/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

const withImages = require('next-images')
module.exports = withImages()

module.exports = {
  images: {
    domains: [
      'images.unsplash.com',
    ],
  }
}

module.exports = nextConfig

