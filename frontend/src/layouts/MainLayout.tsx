import type { ReactNode } from "react";
import Navbar from "../components/Navbar";

type MainLayoutProps = {
  children: ReactNode;
};

function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Navbar />
      {children}
    </div>
  );
}

export default MainLayout;