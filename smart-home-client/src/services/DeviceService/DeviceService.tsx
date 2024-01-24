import customAxios from "../AxiosInterceptor/AxiosInterceptor";


class DeviceService {

    activateAlarm(time: string) {
        return customAxios.put(`/activate_alarm`);
    }
}

export default new DeviceService();