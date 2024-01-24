// DeviceList.tsx
import { Device } from "../../../models/Device";
import DeviceCard from "../DeviceCard/DeviceCard";
import { ItemsListStyle, CircleContainer, InnerCircle } from "./DeviceList.styled";
import React from "react";

export type DeviceListProps = {
    devices: Device[];
    onDetails: (device: Device) => void;
};

const calculateCircleCoordinates = (
    centerX: number,
    centerY: number,
    radius: number,
    angle: number
) => {
    const x = centerX + radius * Math.cos(angle);
    const y = centerY + radius * Math.sin(angle);
    return { x, y };
};

export default function DeviceList({ devices, onDetails }: DeviceListProps) {
    const seenTypes = new Set();
    const filteredDevices = devices.filter((device) => {
        if (!seenTypes.has(device.type)) {
            seenTypes.add(device.type);
            return true;
        }
        return false;
    });

    const [circleCenter, setCircleCenter] = React.useState({ x: 0, y: 0 });

    React.useEffect(() => {
        const handleResize = () => {
            const windowWidth = window.innerWidth;
            const windowHeight = window.innerHeight;

            // Prilagodite ove faktore prema vašim potrebama
            const circleRadiusFactor = 0.4;

            // Izračunavanje centra kružnice
            const circleCenterX = windowWidth / 2.27;
            const circleCenterY = 250;

            setCircleCenter({ x: circleCenterX, y: circleCenterY });
        };

        window.addEventListener("resize", handleResize);

        // Prvo postavljanje kada se komponenta mount-uje
        handleResize();

        // Cleanup event listener-a kada komponenta unmount-uje
        return () => {
            window.removeEventListener("resize", handleResize);
        };
    }, []);

    return (
        <ItemsListStyle>
            <CircleContainer>
                {filteredDevices.map((device, index) => {
                    const circleRadiusFactor = 0.37; // Prilagodite ovaj faktor prema vašim potrebama
                    const circleAngle =
                        (index / filteredDevices.length) * 2 * Math.PI;

                    // Izračunavanje koordinata na spoljnoj kružnici
                    const x =
                        circleCenter.x +
                        circleCenter.x * circleRadiusFactor * Math.cos(circleAngle);
                    const y =
                        circleCenter.y +
                        circleCenter.x * circleRadiusFactor * Math.sin(circleAngle);

                    return (
                        <DeviceCard
                            key={device.type}
                            device={device}
                            onDetails={() => onDetails(device)}
                            coordinates={{ x, y }}
                        />
                    );
                })}
                <InnerCircle>
                    <h3>Devices</h3>
                </InnerCircle>
            </CircleContainer>
        </ItemsListStyle>
    );
}
