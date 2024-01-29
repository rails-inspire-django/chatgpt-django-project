const Path = require("path");
const pwd = process.env.PWD;

// We can add current project paths here
const projectPaths = [
    Path.join(pwd, "./chatgpt_django_app/templates/**/*.html"),
    // add js file paths if you need
];

const contentPaths = [...projectPaths];
console.log(`tailwindcss will scan ${contentPaths}`);

module.exports = {
    content: contentPaths,
    theme: {
        extend: {},
    },
    plugins: [
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
    ],
}
