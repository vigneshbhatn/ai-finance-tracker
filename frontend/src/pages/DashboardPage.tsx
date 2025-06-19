// src/pages/Dashboard.tsx

import { useState } from 'react';
import Header from '../components/Header';
import Navbar from '../components/NavBar';
import NetWorthCard from '../components/NetWordCard';
import ExpenseCard from '../components/ExpenseModal';
import BudgetCard from '../components/BudgetModal';
import ExpenseList from '../components/ExpenseList';

import AddExpenseModal from '../components/AddExpenseModal';
import AddEarningModal from '../components/AddEarningModal';
import SetBudgetModal from '../components/AddBudgetModal';

export default function Dashboard() {
  // Dummy values for now
  const [netWorth, setNetWorth] = useState(15000);
  const [totalExpenses, setTotalExpenses] = useState(4000);
  const [budget, setBudget] = useState(10000);
  const [expenses, setExpenses] = useState([
    { category: 'Groceries', amount: 1200 },
    { category: 'Food', amount: 800 },
    { category: 'Transport', amount: 500 },
  ]);

  // Modal state
  const [showExpenseModal, setShowExpenseModal] = useState(false);
  const [showEarningModal, setShowEarningModal] = useState(false);
  const [showBudgetModal, setShowBudgetModal] = useState(false);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <Navbar />
      <Header name="Viggy" />

      <div className="flex flex-wrap gap-4 mb-6">
        <NetWorthCard netWorth={netWorth} onAddEarning={() => setShowEarningModal(true)} />
        <ExpenseCard total={totalExpenses} onAddExpense={() => setShowExpenseModal(true)} />
        <BudgetCard budget={budget} onSetBudget={() => setShowBudgetModal(true)} />
      </div>

      <div className="flex flex-col md:flex-row gap-4">
        <ExpenseList expenses={expenses} />
        {/* Placeholder for chart or analytics component later */}
        <div className="border rounded-xl p-4 w-full max-w-md shadow">
          <h2 className="text-lg font-semibold">Net Worth vs Expenses</h2>
          <p className="text-sm text-gray-500 mt-2">[Chart coming soon]</p>
        </div>
      </div>

      {/* Modals */}
      <AddExpenseModal open={showExpenseModal} onClose={() => setShowExpenseModal(false)} />
      <AddEarningModal open={showEarningModal} onClose={() => setShowEarningModal(false)} />
      <SetBudgetModal open={showBudgetModal} onClose={() => setShowBudgetModal(false)} />
    </div>
  );
}
