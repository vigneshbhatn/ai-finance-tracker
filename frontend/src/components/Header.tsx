// src/components/Header.tsx
type HeaderProps = {
  name: string;
};

export default function Header({ name }: HeaderProps) {
  return (
    <h1 className="text-2xl font-semibold mb-4">
      Hello There, {name}!
    </h1>
  );
}
