import React, { useState } from "react";

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!username || !password) {
      setError("Please fill out both fields.");
    } else {
      setError("");
      console.log("Logging in:", { username, password });
    }
  };

  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center bg-[#f7f7f7] relative overflow-hidden">
      {/* Animated background blobs */}
      <div className="absolute top-0 -left-40 w-[600px] h-[500px] rounded-full mix-blend-multiply filter blur-2xl opacity-30 animate-float rainbow-blob" />
      <div className="absolute -bottom-32 right-40 w-[600px] h-[600px] bg-[#3730a3] rounded-full mix-blend-multiply filter blur-2xl opacity-40 animate-float animation-delay-3000" />
      <div className="absolute top-1/2 left-1/2 w-[500px] h-[500px] bg-[#3730a3] rounded-full mix-blend-multiply filter blur-2xl opacity-40 animate-float animation-delay-5000" />
      <div className="absolute top-0 -left-40 w-[500px] h-[600px] rounded-full mix-blend-multiply filter blur-2xl opacity-30 animate-float animation-delay-7000 rainbow-blob" />
      
      <div className="w-[450px] mx-4">
        <h1 className="text-3xl font-bold text-[#170F49] mb-4 text-center">
          Sign in to your account
        </h1>
        
        {/* Login container */}
        <div className="relative bg-white/30 backdrop-blur-xl rounded-3xl shadow-xl p-12 border border-white/20">
          <form onSubmit={handleSubmit} className="space-y-6">
            {error && (
              <p className="text-red-500 text-sm mb-4">{error}</p>
            )}
            
            {/* Username field */}
            <div className="space-y-2 w-full">
              <label 
                htmlFor="username" 
                className="block text-sm font-medium text-[#170F49] ml-4"
              >
                Username
              </label>
              <input
                id="username"
                type="text"
                placeholder="Enter username here."
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full px-4 py-4 rounded-full border bg-white shadow-lg focus:outline-none focus:ring-2 focus:ring-[#6366f1] transition-all placeholder:text-[#6F6C90]"
              />
            </div>
            
            {/* Password field */}
            <div className="space-y-2 w-full">
              <label 
                htmlFor="password" 
                className="block text-sm font-medium text-[#170F49] ml-4"
              >
                Password
              </label>
              <input
                id="password"
                type="password"
                placeholder="Enter password here."
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-4 rounded-full border bg-white shadow-lg focus:outline-none focus:ring-2 focus:ring-[#6366f1] transition-all placeholder:text-[#6F6C90]"
              />
            </div>
            
            {/* Submit button */}
            <button
              type="submit"
              className="w-full bg-[#6366f1] shadow-lg text-white py-4 rounded-full hover:bg-[#4f46e5] transition-colors font-medium"
            >
              Sign in
            </button>
          </form>
          
          {/* Info text */}
          <p className="text-[#6F6C8F] text-xs text-center mt-6">
            No account? Contact administrator to manage access.
          </p>
        </div>
      </div>

      {/* Global styles for animations */}
      <style jsx global>{`
        @keyframes float {
          0% {
            transform: translate(0, 0) scale(1);
          }
          25% {
            transform: translate(100px, -100px) scale(1.2);
          }
          50% {
            transform: translate(0, 100px) scale(0.9);
          }
          75% {
            transform: translate(-100px, -50px) scale(1.1);
          }
          100% {
            transform: translate(0, 0) scale(1);
          }
        }
        .animate-float {
          animation: float 15s infinite ease-in-out;
        }
        .animation-delay-3000 {
          animation-delay: -5s;
        }
        .animation-delay-5000 {
          animation-delay: -10s;
        }
        .animation-delay-7000 {
          animation-delay: -15s;
        }
        .rainbow-blob {
          background: conic-gradient(
            from 0deg,
            #ff0000,
            #ff8000,
            #ffff00,
            #00ff00,
            #00ffff,
            #0000ff,
            #8000ff,
            #ff0080,
            #ff0000
          );
          animation: float 15s infinite ease-in-out, spin 15s linear infinite;
        }
        @keyframes spin {
          from {
            transform: rotate(0deg);
          }
          to {
            transform: rotate(360deg);
          }
        }
      `}</style>
    </div>
  );
};

export default LoginPage;