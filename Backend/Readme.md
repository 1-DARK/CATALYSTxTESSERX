# DiagnoAI - Backend API

## Overview

This is the backend service for the DiagnoAI Medical Diagnosis Platform. It provides REST API endpoints for handling various media types, blockchain integration for medical records, and IPFS storage capabilities.

## Technology Stack

- **Framework**: Django with Django REST Framework
- **Database**: SQLite (db.sqlite3)
- **Storage**: IPFS integration for decentralized file storage
- **Blockchain**: Web3 integration with Ethereum (SimpleBackendRegistry contract)

## Core Components

### API Module

- **Serializers**: Handles data serialization for various media types (Text, Image, Audio, Video, PDF)
- **Views**: API endpoints for frontend communication
- **Services**: Business logic implementation
- **Web3**: Blockchain integration services

### Models

The backend supports multiple media types:

- Text documents
- Images
- Video files
- PDF reports

## Key Endpoints

- **/pdf**: Accepts PDF reports from the frontend for IPFS/Blockchain storage
- Transaction verification endpoints for blockchain data retrieval

## Features

- **Media Processing**: Handles various media formats for medical diagnostics
- **Blockchain Integration**: Secures medical reports using smart contracts
- **IPFS Storage**: Decentralized storage for medical documents
- **Transaction Verification**: Validate blockchain transactions for authenticity
- **Error Handling**: Robust error management for network and processing issues

## Development Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run migrations:

```bash
python manage.py migrate
```

3. Start development server:

```bash
python manage.py runserver
```

## API Integration

The backend provides integration points for the following frontend features:

- PDF report generation and storage
- Blockchain transaction verification
- Media file processing for diagnostic tools

## Security Considerations

- Implements encryption for sensitive medical data
- Uses blockchain technology for immutable record-keeping
- Generates verification IDs for patient records

## License

This project is proprietary. All rights reserved.
