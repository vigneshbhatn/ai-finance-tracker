// src/components/Navbar.tsx
export default function Navbar() {
  return (
    <nav className="flex space-x-4 mb-6 text-blue-500 font-medium">
      <a href="#" className="hover:underline">Dashboard</a>
      <a href="#" className="hover:underline">Expenses</a>
      <a href="#" className="hover:underline">Budget</a>
      <a href="#" className="hover:underline">Earning</a>
    </nav>
  );
}
