/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primaryDark': '#1F2029',
        'primaryLight': '#FCFEFF',
        'secondaryDark': '#2C2A37'
      },
      backgroundImage: {
        'signup': "url('/assets/signup.jpg')",
      }
    },
  },
  plugins: [],
}
