// src/components/NetWorthCard.tsx
type NetWorthCardProps = {
  netWorth: number;
  onAddEarning: () => void;
};

export default function NetWorthCard({ netWorth, onAddEarning }: NetWorthCardProps) {
  return (
    <div className="border rounded-xl p-4 w-full max-w-sm shadow">
      <h2 className="text-lg font-semibold">Net Worth</h2>
      <p className="text-2xl font-bold mb-2">₹{netWorth}</p>
      <button 
        onClick={onAddEarning} 
        className="bg-blue-500 text-white px-4 py-1 rounded"
      >
        Add Earning +
      </button>
    </div>
  );
}
