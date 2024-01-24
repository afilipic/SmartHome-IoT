import { useNavigate } from "react-router-dom";
import DeviceList from "../../components/device/DeviceList/DeviceList";
import { StyledPage } from "../../components/shared/styled/SharedStyles.styled";
import { devices } from "../../utils/data";
import { Device } from "../../models/Device";
import { GlobalStyle, StyledButton, StyledPanel } from "./DevicePage.styled";
import { CustomButton } from "../HomePage/HomePage.styled";
import { SetStateAction, useState } from "react";
import Modal from "../../components/shared/modal/Modal";
import AlarmForm from "../../components/device/AlarmForm/AlarmForm";
import SecurityModeForm from "../../components/device/SecurityModeForm/SecurityModeForm";

export default function DevicePage() {
    const navigate = useNavigate();

    const handleDetails = (device: Device) => {
        navigate(`/devices/${device.type}`)
    };

    // Držači stanja za modal i vrednost alarma
    const [isAlarmModalOpen, setIsAlarmModalOpen] = useState(false);
    const [isSecurityModeModalOpen, setIsSecurityModeModalOpen] = useState(false);
    const [alarmTime, setAlarmTime] = useState("");
    const [securityCode, setSecurityCode] = useState("");

    // Funkcija koja će se pozvati kada se postavi alarm
    const handleSetAlarm = (time:string) => {
        setAlarmTime(time);
        // Dodajte ovde logiku za postavljanje alarma
        console.log("Alarm set:", time);
        setIsAlarmModalOpen(false); // Zatvaranje modala nakon postavljanja alarma
    };

    const handleSetSecurityCode = (code: string) => {
        setSecurityCode(code);
        console.log("Security code set:", code);
        setIsSecurityModeModalOpen(false);
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
            </StyledPage>
            <Modal isVisible={isAlarmModalOpen} onClose={() => setIsAlarmModalOpen(false)}>
                <AlarmForm onSubmit={handleSetAlarm} />
            </Modal>
            <Modal isVisible={isSecurityModeModalOpen} onClose={() => setIsSecurityModeModalOpen(false)}>
                <SecurityModeForm onSubmit={handleSetSecurityCode} />
            </Modal>
        </>
        
    )
}