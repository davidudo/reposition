function getApiDomain() {
  const PROD_API_DOMAIN = 'https://reposition.onrender.com';
  const DEV_API_DOMAIN = 'http://127.0.0.1:8000';

  if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
    return DEV_API_DOMAIN;
  } else {
    return PROD_API_DOMAIN;
  }
}

export const API_DOMAIN = getApiDomain();
