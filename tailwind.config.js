'use strict';

module.exports = {
    content: [
        './**/templates/**/*.{html,js}',
        './templates/**/*.{html,js}'
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
};
