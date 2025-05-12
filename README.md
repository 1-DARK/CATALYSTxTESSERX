# CATALYSTxTESSERX

# DiagnoAI - Medical Diagnosis Platform

## Overview

DiagnoAI is a comprehensive web-based medical diagnosis platform that integrates interactive symptom checking, AI-driven diagnostics, personalized wellness plans, and blockchain-based transaction verification. The platform empowers users to identify potential health conditions, access tailored health recommendations, and securely store medical reports. It features an intuitive, responsive interface suitable for both mobile and desktop users, with a robust backend to handle media processing, decentralized storage, and blockchain integration.



https://github.com/user-attachments/assets/cc42b882-e15b-41c6-aa87-47af05f2bd13



## File Structure

### Frontend
1. **index.html** - Main landing page with hero section and feature highlights.
2. **FrontSYM.html** - Front view of the human body with interactive symptom checker.
3. **BackSYM.html** - Back view of the human body with interactive symptom checker.
4. **verify-trxn.html** - Blockchain transaction verification interface.
5. **Vision.html** - "Our Services" page with detailed feature explanations.

### Backend
- **Django Project**: Core backend service with REST API endpoints.
- **db.sqlite3**: SQLite database for development.
- **requirements.txt**: Lists Python dependencies for backend setup.

## Technology Stack

### Frontend
- **HTML5, CSS3, JavaScript**: Core structure and interactivity.
- **Bootstrap**: Responsive layouts and mobile-friendly design.
- **GSAP**: Animations, scroll effects, and floating images in the hero section.
- **jsPDF**: PDF report generation.
- **Font Awesome**: Icons for UI elements.
- **Google Fonts**: Custom typography for consistent branding.

### Backend
- **Framework**: Django with Django REST Framework.
- **Database**: SQLite (db.sqlite3) for development.
- **Storage**: IPFS for decentralized file storage.
- **Blockchain**: Web3 integration with Ethereum (SimpleBackendRegistry contract).
- **Dependencies**: Listed in `requirements.txt`.

## Key Features

### Frontend Features
1. **Interactive Body Map Symptom Checker**:
   - Front and back human body views with clickable SVG diagrams (`FrontSYM.html`, `BackSYM.html`).
   - Real-time diagnostic suggestions based on selected body parts (e.g., head, chest, back, legs).
   - Visual feedback with hover effects and color changes on selection.
   - Displays related conditions, symptoms, treatments, and severity indicators (low, medium, high).

2. **Search Functionality**:
   - Real-time filtering search bar for conditions and symptoms, accessible on `FrontSYM.html` and `BackSYM.html`.

3. **Personalized Wellness Plans**:
   - AI-generated nutrition recommendations tailored to specific conditions.
   - Condition-specific fitness routines, including anti-inflammatory and joint-friendly options.

4. **AI Image Analysis**:
   - X-ray and medical image interpretation with confidence percentage indicators.
   - Detection of potential health issues based on uploaded images.

5. **Natural Language Diagnostics**:
   - Text-based symptom analysis via a chat-style interface.
   - Disease probability percentages with educational explanations.

6. **Report Generation and Blockchain Integration for securing sensitive input data(image/video) for user input history**:
   - Generate PDF reports of selected conditions using jsPDF.
   - Upload video/image/reports to backend for IPFS/Blockchain storage via `/pdf` endpoint.
   - Display processing status, including IPFS CID and blockchain transaction hash.
   - Transaction verification interface (`verify-trxn.html`) for validating transaction hashes, showing status, block number, and addresses.

7. **Specialist Recommendations**:
   - Provides doctor names, specialties, hospital information, and contact details.
   - Integrated into condition details for actionable follow-up.

8. **Emergency Protocols**:
   - Dedicated section in `FrontSYM.html` for emergency guidance and first aid recommendations.

9. **Video Chatbot**:
   - Video messaging for users to record and send visual demonstrations of physical symptoms.

### Backend Features
1. **Media Processing**:
   - Handles various media formats (Text, Image, Audio, Video, PDF) for diagnostic tools.
   - Serializers and services for data processing and validation.

2. **Blockchain Integration**:
   - Secures medical video/image input reports using Ethereum smart contracts (SimpleBackendRegistry).
   - Generates verification IDs for patient records.

3. **IPFS Storage**:
   - Decentralized storage for medical documents, accessible via `/pdf` endpoint.

4. **Transaction Verification**:
   - Validates blockchain transactions for authenticity, supporting the `verify-trxn.html` interface.

5. **Error Handling**:
   - Robust error management for network issues, backend failures, and invalid transaction hashes.

## API Endpoints
- **/pdf**: Accepts PDF reports from the frontend for IPFS/Blockchain storage.
- **Transaction Verification**: Retrieves blockchain data for transaction validation (e.g., status, block number, addresses).

## Usage Instructions

### Frontend
1. **Navigation**:
   - Use the consistent navbar across all pages to switch between Home (`index.html`), Our Services (`Vision.html`), Front Symptoms (`FrontSYM.html`), Back Symptoms (`BackSYM.html`), and Transaction Verification (`verify-trxn.html`).

2. **Symptom Checker**:
   - Open `FrontSYM.html` or `BackSYM.html` in a web browser.
   - Click on a body part in the interactive SVG diagram to view related conditions, symptoms, treatments, and first aid recommendations.
   - Use the search bar to find conditions by name or symptom.
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

### Backend
1. **Setup**:
   - Install dependencies: `pip install -r requirements.txt`.
   - Run migrations: `python manage.py migrate`.
   - Start the development server: `python manage.py runserver`.

2. **Integration**:
   - The backend supports frontend features like PDF report storage, blockchain transaction verification, and media file processing.
   - Ensure the `/pdf` endpoint is accessible for report uploads and IPFS/Blockchain storage.

## Development Notes

### Frontend
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

4. **Styling Features**:
   - Dark theme with customizable accent colors via CSS variables.
   - Animated transitions, hover effects, and scroll-triggered animations.
   - Mobile menu toggles for smaller screens.

### Backend
1. **Security Considerations**:
   - Implements encryption for sensitive medical data.
   - Uses blockchain for immutable record-keeping.
   - Generates unique verification IDs for patient records.

2. **Scalability**:
   - SQLite is used for development; consider PostgreSQL or similar for production.
   - Optimize IPFS and blockchain interactions for performance in high-traffic scenarios.

3. **Error Handling**:
   - Includes robust error handling for network issues, backend failures, and invalid transaction hashes.
   - Displays user-friendly error messages and status indicators.

## Security Considerations
- **Frontend**: Secure handling of user inputs in search bars and chat interfaces to prevent injection attacks.
- **Backend**: Encryption for sensitive medical data and immutable blockchain storage for report integrity.
- **API**: Secure API endpoints with proper authentication and validation.

## License
This project is proprietary code. All rights reserved by ACMECorp. For inquiries about use or modification, contact the project maintainers.


