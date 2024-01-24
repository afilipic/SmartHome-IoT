// SecurityModeForm.js

import React, { useState } from "react";
import { StyledForm, StyledInput, StyledButton } from "./SecurityModeForm.styled";

// Definišite tip za onSubmit prop
type SecurityModeFormProps = {
    onSubmit: (code: string) => void;
};

const SecurityModeForm = ({ onSubmit }: SecurityModeFormProps) => {
    const [securityCode, setSecurityCode] = useState("");

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        // Samo pozovite onSubmit funkciju ako je kod tačno četvorocifren
        if (securityCode.length === 4) {
            onSubmit(securityCode);
        } else {
            console.log("Unesite tačno četvorocifreni kod.");
        }
    };

    return (
        <StyledForm onSubmit={handleSubmit}>
            <label htmlFor="securityCode">Enter Security Code:</label>
            <StyledInput
                type="text"
                id="securityCode"
                value={securityCode}
                onChange={(e) => setSecurityCode(e.target.value)}
                maxLength={4} // Postavite maksimalnu dužinu na 4
            />
            <StyledButton type="submit">Save</StyledButton>
        </StyledForm>
    );
};

export default SecurityModeForm;
