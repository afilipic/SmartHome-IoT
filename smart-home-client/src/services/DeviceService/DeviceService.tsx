import customAxios from "../AxiosInterceptor/AxiosInterceptor";


class DeviceService {
    setScheduleAlarm(time: string) {
        return customAxios.put(`/schedule_alarm/${time}`);
    }

    activateAlarm() {
        return customAxios.put(`/activate_alarm`);
    }
    deactivateAlarm() {
        return customAxios.put(`/deactivate_alarm`);
    }

}

export default new DeviceService();