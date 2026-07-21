/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "standalone",
  // The dashboard reads the operating docs from disk on every request; nothing
  // it renders may be cached across sessions.
  poweredByHeader: false,
};

export default nextConfig;
