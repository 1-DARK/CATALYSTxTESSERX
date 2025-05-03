
# DiagnoAI - Medical Diagnosis Platform

## Overview

DiagnoAI is a comprehensive web-based medical diagnosis platform that combines interactive symptom checking, AI-driven diagnostics, personalized wellness plans, and blockchain-based transaction verification. The platform empowers users to identify potential health conditions, access tailored health recommendations, and securely store medical reports. It features an intuitive interface with responsive design, suitable for both mobile and desktop users.

## File Structure

1. **index.html** - Main landing page with hero section and feature highlights.
2. **FrontSYM.html** - Front view of the human body with interactive symptom checker.
3. **BackSYM.html** - Back view of the human body with interactive symptom checker.
4. **verify-trxn.html** - Blockchain transaction verification interface.
5. **Vision.html** - "Our Services" page with detailed feature explanations.

## Key Features

### Core Functionality

1. **Interactive Body Map Symptom Checker**:
   - Front and back human body views with clickable SVG diagrams.
   - Real-time diagnostic suggestions based on selected body parts (e.g., head, chest, back, legs).
   - Visual feedback with hover effects and color changes on selection.
   - Displays related conditions, symptoms, treatments, and severity indicators (low, medium, high).

2. **Search Functionality**:
   - Search across all conditions and symptoms using a real-time filtering search bar.
   - Accessible on both `FrontSYM.html` and `BackSYM.html`.

3. **Personalized Wellness Plans**:
   - AI-generated nutrition recommendations tailored to specific conditions.
   - Condition-specific fitness routines, including anti-inflammatory and joint-friendly options.

4. **AI Image Analysis**:
   - X-ray and medical image interpretation with confidence percentage indicators.
   - Detection of potential health issues based on uploaded images.

5. **Natural Language Diagnostics**:
   - Text-based symptom analysis via a chat-style interface.
   - Disease probability percentages with educational explanations.

6. **Report Generation and Blockchain Integration**:
   - Generate PDF reports of selected conditions using the jsPDF library.
   - Upload reports to backend for IPFS/Blockchain storage via `/pdf` endpoint.
   - Display processing status, including IPFS CID and blockchain transaction hash.
   - Transaction verification interface (`verify-trxn.html`) for validating transaction hashes, showing status, block number, and addresses.

7. **Specialist Recommendations**:
   - Provides doctor names, specialties, hospital information, and contact details.
   - Integrated into condition details for actionable follow-up.

8. **Emergency Protocols**:
   - Dedicated section in `FrontSYM.html` for emergency guidance and first aid recommendations.

### Technical Implementation

- **Frontend Technologies**:
  - HTML5, CSS3, JavaScript for core structure and interactivity.
  - Bootstrap for responsive layouts and mobile-friendly design.
  - GSAP for animations, scroll effects, and floating images in the hero section.
  - jsPDF for PDF report generation.
  - Font Awesome for icons and Google Fonts for custom typography.

- **Styling Features**:
  - Dark theme with customizable accent colors via CSS variables.
  - Animated transitions, hover effects, and scroll-triggered animations.
  - Media queries for adaptive layouts across device sizes.
  - Mobile menu toggles for smaller screens.

- **Backend Integration**:
  - PDF upload endpoint (`/pdf`) for IPFS/Blockchain storage.
  - Transaction verification API for blockchain data retrieval.
  - Error handling for network issues and backend failures.

- **Interactive Elements**:
  - Animated hero section with dynamic visuals.
  - Interactive body maps with SVG-based click regions.
  - Real-time search and filtering for conditions and symptoms.
  - Chat-style interface for natural language diagnostics.

## Usage Instructions

1. **Navigation**:
   - Use the consistent navbar across all pages to switch between sections: Home, Our Services (`Vision.html`), Front Symptoms (`FrontSYM.html`), Back Symptoms (`BackSYM.html`), and Transaction Verification (`verify-trxn.html`).

2. **Symptom Checker**:
   - Open `FrontSYM.html` or `BackSYM.html` in a web browser.
   - Click on a body part in the interactive SVG diagram to view related conditions, symptoms, treatments, and first aid recommendations.
   - Alternatively, use the search bar to find conditions by name or symptom.
   - View specialist recommendations and severity indicators.

3. **Report Generation**:
   - Click "Send Report" to generate a PDF of selected conditions.
   - The PDF is sent to the backend for IPFS/Blockchain storage.
   - Check the "Report Processing Status" section for IPFS CID and blockchain transaction hash.

4. **Transaction Verification**:
   - Navigate to `verify-trxn.html`.
   - Enter a valid transaction hash in the input field and click "Verify".
   - View transaction details, including status, block number, and addresses.

5. **Wellness Plans and Image Analysis**:
   - Access personalized nutrition and fitness plans via `Vision.html` or symptom checker pages.
   - Upload medical images for AI-driven analysis, with results showing confidence percentages and potential issues.

## Development Notes

1. **Dependencies**:
   - Ensure CDN links for Bootstrap, GSAP, Font Awesome, and jsPDF are accessible.
   - Font imports from Google Fonts for consistent typography.
   - Replace placeholder images with actual medical illustrations for production.

2. **Customization**:
   - Modify color schemes in CSS variables for branding consistency.
   - Adjust GSAP animation timings for optimal user experience.
   - Update the medical database (stored as JavaScript objects) to expand condition and symptom coverage.

3. **Responsive Considerations**:
   - Media queries ensure compatibility across device sizes.
   - Stacked layouts and mobile menu toggles enhance usability on narrow viewports.
   - Test thoroughly on mobile devices to ensure touch interactions work smoothly.

4. **Error Handling**:
   - Includes robust error handling for network issues, backend failures, and invalid transaction hashes.
   - Displays user-friendly error messages and status indicators.

## Future Enhancements

1. Integrate actual backend API endpoints for real-time data processing.
2. Implement user authentication and patient history tracking.
3. Expand the medical database with more conditions and symptoms.
4. Add multi-language support for broader accessibility.
5. Enhance mobile experience with native-like features.
6. Incorporate advanced visualizations for condition data.
7. Implement real medical image analysis with trained AI models.

## License

This project is proprietary code. All rights reserved by ACMECorp (as noted in the footer). For use or modification, please contact the project maintainers.

## Disclaimer

This application is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.

---

For detailed implementation, refer to the individual HTML files and their inline documentation. The system is modular, with shared components (navbar, footer) maintained consistently across pages.
