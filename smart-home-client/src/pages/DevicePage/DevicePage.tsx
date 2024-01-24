import { useNavigate } from "react-router-dom";
import DeviceList from "../../components/device/DeviceList/DeviceList";
import { StyledPage } from "../../components/shared/styled/SharedStyles.styled";
import { devices } from "../../utils/data";
import { Device } from "../../models/Device";
import { GlobalStyle } from "./DevicePage.styled";

export default function DevicePage() {
    const navigate = useNavigate();

    const handleDetails = (device: Device) => {
        navigate(`/devices/${device.type}`)
    };

    return (
        <>
            <GlobalStyle />
            <StyledPage>
                
                <DeviceList
                    devices={devices}
                    onDetails={handleDetails} />
            </StyledPage>
        </>
        
    )
}