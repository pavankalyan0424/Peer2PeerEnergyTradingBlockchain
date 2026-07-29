import { BrowserRouter, Route, Routes } from "react-router-dom";
import MarketplacePage from "./pages/MarketplacePage";
import Navbar from "./components/Navbar/Navbar";
import BuyerPage from "./pages/BuyerPage";
import AdminPage from "./pages/AdminPage";


function App() {
  return <BrowserRouter>
    <Navbar />
    <Routes>
      <Route path="/" element={<MarketplacePage />} />
      <Route path="/buyer" element={<BuyerPage />} />
      <Route path="/admin" element={<AdminPage />} />
    </Routes>
  </BrowserRouter >;
}
export default App;