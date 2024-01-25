import { useNavigate } from "react-router-dom";
import DeviceList from "../../components/device/DeviceList/DeviceList";
import { StyledPage } from "../../components/shared/styled/SharedStyles.styled";
import { devices, urls } from "../../utils/data";
import { Device } from "../../models/Device";
import { GlobalStyle, StyledButton, StyledPanel, StyledPanel2 } from "./DevicePage.styled";
import { CustomButton } from "../HomePage/HomePage.styled";
import { SetStateAction, useEffect, useState } from "react";
import Modal from "../../components/shared/modal/Modal";
import AlarmForm from "../../components/device/AlarmForm/AlarmForm";
import SecurityModeForm from "../../components/device/SecurityModeForm/SecurityModeForm";
import { Socket, io } from "socket.io-client";
import DeclineAlarmForm from "../../components/device/DeclineAlarmForm/DeclineAlarmForm";
import DeviceService from "../../services/DeviceService/DeviceService";

export default function DevicePage() {
    const navigate = useNavigate();

    const handleDetails = (device: Device) => {
        navigate(`/devices/${device.type}`)
    };

    // Držači stanja za modal i vrednost alarma
    const [isAlarmModalOpen, setIsAlarmModalOpen] = useState(false);
    const [isSecurityModeModalOpen, setIsSecurityModeModalOpen] = useState(false);
    const [isAlarmActive, setIsAlarmActive] = useState(false);
    const [alarmTime, setAlarmTime] = useState("");
    const [securityCode, setSecurityCode] = useState("");
    const [socket, setSocket] = useState<Socket | null>(null);
    const [enteredPin, setEnteredPin] = useState("");
    const [pin, setPin] = useState("1111");

    useEffect(() => {
        console.log(pin);
        const socket = io("http://localhost:8085");
        socket.on("connect", () => {
            console.log("Connected to WebSocket");
            socket.emit("subscribe", "alarm");
        });

        socket.on("alarm", (message) => {
            console.log("Connected to alarm");
            setIsAlarmActive(true);
        });
        socket.on("deactivate_alarm", (message) => {
            console.log("Disconnect to alarm");
            setIsAlarmActive(false);
        });
        socket.on("activate_alarm", (message) => {
            console.log("Activate to alarm");
            setIsAlarmActive(false);
        });

        setSocket(socket);

        return () => {
            socket.disconnect();
        };
    }, []);



    const handleSetAlarm = (time: string) => {
        setAlarmTime(time);
        // Dodajte ovde logiku za postavljanje alarma
        DeviceService.setScheduleAlarm(time).then(response => {
            console.log(response.data, "bbbbbbbbb");
            setIsAlarmModalOpen(false);
        }).catch(error => {
            console.error("Error: ", error)
        })
        console.log("Alarm set:", time);
    };

    const handleSetSecurityCode = (code: string) => {
        // Provera da li je uneti PIN tačan pre nego što se promeni vrednost
        if (code.length === 4 && /^\d+$/.test(code)) {
            setSecurityCode(code);
            //setEnteredPin(code); // Čuvanje unetog PIN-a
            setPin(code); // Čuvanje novog PIN-a
            console.log("Security code set:", code);
            setIsSecurityModeModalOpen(false);
        } else {
            console.log("Invalid security code. Please enter a valid 4-digit PIN.");
            // Dodajte logiku za obaveštavanje korisnika o nevažećem PIN-u
        }
    };

    const handleActiveAlarm = (enteredPin: string) => {
        if (enteredPin === pin) {
            console.log("Alarm deactivated successfully.");
            // Dodajte logiku za deaktivaciju alarma
            DeviceService.deactivateAlarm().then(response => {
                console.error(response, "aaaaaaaaaaaa")
            }).catch(error => {
                console.error("Error: ", error)
            })
            if (socket) {
                socket.off("alarm");
            }
        } else {
            console.log("Invalid PIN. Alarm deactivation failed.");
            // Dodajte logiku za obaveštavanje korisnika o nevažećem PIN-u
        }
        setIsAlarmActive(false);
        setEnteredPin(""); // Resetujte enteredPin nakon upoređivanja
    };

    const handleNumberOfPeopleClick = () => {
        // Extract the URL for "NoT"
        const notUrl = "NoP";

        // Check if the URL is available
        if (notUrl) {
            // Redirect to the URL
            navigate(notUrl);
        } else {
            console.error("No URL found for NoP");
        }
    };

    return (
        <>
            <GlobalStyle />
            <StyledPage>

                <DeviceList
                    devices={devices}
                    onDetails={handleDetails} />
                <StyledPanel>
                    <h2>Alarm settings</h2>
                    <CustomButton onClick={() => setIsAlarmModalOpen(true)}>
                        Alarm
                    </CustomButton>
                    <CustomButton onClick={() => setIsSecurityModeModalOpen(true)}>
                        Security mode
                    </CustomButton>
                </StyledPanel>
                <StyledPanel2>
                    <h2>Other</h2>
                    <CustomButton onClick={handleNumberOfPeopleClick}>
                        Number of people
                    </CustomButton>
                </StyledPanel2>
            </StyledPage>
            <Modal isVisible={isAlarmModalOpen} onClose={() => setIsAlarmModalOpen(false)}>
                <AlarmForm onSubmit={handleSetAlarm} />
            </Modal>
            <Modal isVisible={isSecurityModeModalOpen} onClose={() => setIsSecurityModeModalOpen(false)}>
                <SecurityModeForm onSubmit={handleSetSecurityCode} />
            </Modal>
            <Modal isVisible={isAlarmActive} onClose={() => setIsAlarmActive(false)}>
                <DeclineAlarmForm onSubmit={handleActiveAlarm} />
            </Modal>
        </>
    );
}