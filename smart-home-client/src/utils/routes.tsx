import React from "react";
import { Routes, Route } from "react-router-dom";
import HomePage from "../pages/HomePage/HomePage";
import DevicePage from "../pages/DevicePage/DevicePage";
import DeviceDetailsPage from "../pages/DeviceDetailsPage/DeviceDetailsPage";



export default function MyRoutes() {
  return (
    <Routes>
      <Route path="" element={<HomePage />} />
      <Route path="/devices" element={<DevicePage />} />
      <Route path="devices/:deviceId" element={<DeviceDetailsPage />} />
    </Routes>
  );
}
