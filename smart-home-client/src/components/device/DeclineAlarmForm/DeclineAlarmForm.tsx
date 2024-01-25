// AlarmForm.js

import React, { useState } from "react";
import { StyledForm, StyledInput, StyledButton } from "./DeclineAlarmForm.styled";

// Define the type for the onSubmit prop
type AlarmFormProps = {
    onSubmit: (time: string) => void;
};

const DeclineAlarmForm = ({ onSubmit }: AlarmFormProps) => {
    const [securityCode, setSecurityCode] = useState("");

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        onSubmit(securityCode);
    };

    return (
        <StyledForm onSubmit={handleSubmit}>
            <h2 style={{ color: '#b4e854' }}>Turn off alarm</h2>
            <StyledInput
                type="text"
                id="securityCode"
                value={securityCode}
                onChange={(e) => setSecurityCode(e.target.value)}
                maxLength={4} // Postavite maksimalnu dužinu na 4
            />
            <StyledButton type="submit">Turn off</StyledButton>
        </StyledForm>
    );
};

export default DeclineAlarmForm;
