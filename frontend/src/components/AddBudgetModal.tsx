// src/components/SetBudgetModal.tsx

type Props = {
  open: boolean;
  onClose: () => void;
};

export default function SetBudgetModal({ open, onClose }: Props) {
  if (!open) return null;

  return (
    <div className="fixed inset-0 flex justify-center items-center bg-black bg-opacity-50 z-50">
      <div className="bg-white rounded-xl p-6 w-[90%] max-w-md">
        <h2 className="text-xl font-bold mb-4">Set Budget</h2>
        <input
          type="number"
          placeholder="Enter budget amount"
          className="w-full mb-4 p-2 border rounded"
        />
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="text-sm bg-gray-200 px-4 py-1 rounded">
            Cancel
          </button>
          <button className="text-sm bg-blue-500 text-white px-4 py-1 rounded">
            Save
          </button>
        </div>
      </div>
    </div>
  );
}
