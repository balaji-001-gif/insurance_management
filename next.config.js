/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Enable static export for GitHub Pages
  output: 'export',
  // Disable image optimization for static export
  images: {
    unoptimized: true,
  },
  // Base path for GitHub Pages (update this to your repo name if needed)
  // basePath: '/g0dm0d3',
  // Trailing slash for GitHub Pages compatibility
  trailingSlash: true,
  // Skip type checking during build (handled separately)
  typescript: {
    ignoreBuildErrors: true,
  },
  eslint: {
    ignoreDuringBuilds: true,
  },
}

module.exports = nextConfig
