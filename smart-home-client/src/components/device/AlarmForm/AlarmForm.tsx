// AlarmForm.js

import React, { useState } from "react";
import { StyledForm, StyledInput, StyledButton } from "./AlarmForm.styled";

// Define the type for the onSubmit prop
type AlarmFormProps = {
    onSubmit: (time: string) => void;
};

const AlarmForm = ({ onSubmit }: AlarmFormProps) => {
    const [alarmTime, setAlarmTime] = useState("");

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        // Call the onSubmit function with the alarmTime
        onSubmit(alarmTime);
    };

    return (
        <StyledForm onSubmit={handleSubmit}>
            <label htmlFor="alarmTime">Set Alarm Time:</label>
            <StyledInput
                type="time"
                id="alarmTime"
                value={alarmTime}
                onChange={(e) => setAlarmTime(e.target.value)}
            />
            <StyledButton type="submit">Save</StyledButton>
        </StyledForm>
    );
};

export default AlarmForm;
