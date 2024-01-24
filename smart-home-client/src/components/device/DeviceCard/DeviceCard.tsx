// DeviceCard.tsx
import { Device } from "../../../models/Device";
import { Card } from "./DeviceCard.styled";

export type DeviceCardProps = {
    device: Device;
    onDetails?: (device: Device) => void;
    coordinates?: { x: number; y: number };
}

export default function DeviceCard({ device, onDetails, coordinates }: DeviceCardProps) {
    const handleOnDetails = () => {
        if (onDetails) {
            onDetails(device);
        }
    }
    return (
        <Card onClick={handleOnDetails} style={{ position: "absolute", left: coordinates?.x, top: coordinates?.y }}>
            <h3>{device.type}</h3>
        </Card>
    );
}
