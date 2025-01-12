
# Subdomain Enumeration Tool

A comprehensive tool for subdomain enumeration using a combination of tools like Subfinder, Assetfinder, PureDNS, Dnsx, and Httpx for validation. This tool is designed to simplify the process of finding, validating, and resolving subdomains for penetration testing, security assessments, and reconnaissance purposes.

### Features
Subdomain Enumeration using:
- **Subfinder** 
- **AssetFinder**
- **PureDNS**

Subdomain Validation using:
- **Dnsx**
- **Httpx**

### Prerequisites
Ensure all tools are installed and available in your PATH:

#### Subfinder
   ```bash
   go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
   ```
#### Assetfinder  
```bash
go install github.com/tomnomnom/assetfinder@latest  
```

#### PureDNS  
```bash
go install github.com/d3mondev/puredns/v2@latest  
```

#### Dnsx  
```bash
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest  
```

#### Httpx  
```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest  
```
#### Verify the installation of tools:

```bash
subfinder -h  
assetfinder -h  
puredns -h  
dnsx -h  
httpx -h
```
### AutoSub Installation
   ```bash
    git clone https://github.com/Sudo-Sakib/AutoSub1.git
    cd AutoSub1
    pip3 install -r requirements.txt
   ```  

## Usage

```bash
python3 main.py
```

## Workflow
- Subfinder, Assetfinder, and PureDNS are executed to enuemrate and resolve subdomains.
- Results from all tools are merged and deduplicated.
- Httpx and dnsx validates live subdomains.

### Output
The tool generates output in a directory named <domain>_<timestamp> with the following files:
- subfinder_output.txt - Raw output from Subfinder.
- assetfinder_output.txt - Raw output from Assetfinder.
- puredns_output.txt - Raw output from PureDNS.
- merged_output.txt - Deduplicated subdomains from all tools.
- valid_domains.txt - Live subdomains validated using Httpx.

#### Feel free to contribute to this project by:

- Adding new tools or features.
- Reporting issues or suggesting improvements.
- Fork the repository, create a feature branch, and submit a pull request!


