import styled from "styled-components";
export const PanelsContainer = styled.div`
    display: flex;
    flex-wrap: wrap;
    gap: 20px; 
    justify-content: center;
    background-color: #111217;
`;
export const TopSection = styled.div`
  width: 100%;
  height: 30vh;
  background-color: ${({ theme }) => theme.colors.secondColor};
`;