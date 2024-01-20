#!/bin/bash
# Set the pipefail option.
set -o pipefail

# Get the Vercel API endpoints.
GET_DEPLOYMENTS_ENDPOINT="https://api.vercel.com/v6/deployments"
DELETE_DEPLOYMENTS_ENDPOINT="https://api.vercel.com/v13/deployments"

# Create a list of deployments.
deployments=$(curl -s -X GET "$GET_DEPLOYMENTS_ENDPOINT/?projectId=$VERCEL_PROJECT_ID&teamId=$VERCEL_ORG_ID" -H "Authorization: Bearer $VERCEL_TOKEN ")

echo $deployments

# Filter for deployments that have (meta.branch_name or meta.githubCommitRef) === BRANCH_NAME.
filtered_deployments=$(echo "$deployments" | jq --arg BRANCH_NAME "$BRANCH_NAME" '[.deployments[] | select((.meta.branch_name // "" | contains($BRANCH_NAME)) or (.meta.githubCommitRef // "" | contains($BRANCH_NAME))) | .uid] | join(",")')
echo $filtered_deployments

filtered_deployments="${filtered_deployments//\"/}" # Remove double quotes

echo $filtered_deployments

# Clears the values from filtered_deployments
IFS=',' read -ra values <<<"$filtered_deployments"

echo "BRANCH_NAME ${BRANCH_NAME}"
echo "Filtered deployments ${filtered_deployments}"

# Iterate over the filtered deployments list.
for uid in "${values[@]}"; do
    echo "Deleting ${uid}"

    delete_url=${DELETE_DEPLOYMENTS_ENDPOINT}/${uid}?teamId=${VERCEL_ORG_ID}
    echo $delete_url

    # Make DELETE a request to the /v13/deployments/{id} endpoint.
    curl -X DELETE $delete_url -H "Authorization: Bearer $VERCEL_TOKEN"

    echo "Deleted!"
done
