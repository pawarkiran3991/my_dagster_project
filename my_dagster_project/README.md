# Dagster + Snowflake + dbt Learning Project

This is a complete Dagster project integrated with Snowflake and dbt, designed for learning and testing Dagster+ deployment capabilities.

## 📋 Project Overview

This project demonstrates:
- **Dagster Assets**: Data pipeline orchestration
- **Snowflake Integration**: Cloud data warehouse connectivity
- **dbt Models**: Data transformations with staging and marts layers
- **Dagster+ Deployment**: CI/CD with GitHub Actions
- **Analytics Pipeline**: End-to-end data processing workflow

## 🏗️ Architecture

```
Snowflake Data Warehouse (DBT_SNF)
│
├── Staging Models (Views)
│   ├── stg_customers
│   └── stg_orders
│
├── Marts Models (Tables)
│   └── customer_summary
│
└── Dagster Assets
    ├── dbt models pipeline
    ├── customer_analytics_report
    └── snowflake_connection_test
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+ 
- Access to Snowflake account: `PHWYUBU-GR70594`
- Git repository on GitHub
- Dagster+ account (for deployment)

### 1. Local Development Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd my_dagster_project

# Install dependencies
pip install -e ".[dev]"

# Copy environment variables
cp .env.example .env

# Start Dagster development server
dagster dev
```

Visit `http://localhost:3000` to access the Dagster UI.

### 2. Snowflake Configuration

The project is pre-configured with your Snowflake credentials:
- **Account**: `PHWYUBU-GR70594`
- **User**: `KPAWAR9428`
- **Database**: `DBT_SNF`
- **Schema**: `DBT_SNF_SC`
- **Warehouse**: `COMPUTE_WH`
- **Authentication**: External Browser

### 3. dbt Setup

The dbt project includes:
- **Profiles**: Pre-configured for your Snowflake instance
- **Models**: Sample staging and marts models
- **Project Structure**: Standard dbt layout with proper materialization

## 📊 Data Pipeline

### Assets Included

1. **`my_dbt_assets`**: Runs all dbt models
2. **`customer_analytics_report`**: Generates analytics from dbt models
3. **`snowflake_connection_test`**: Validates Snowflake connectivity

### Sample Data Models

- **Staging Layer**: 
  - `stg_customers`: Customer master data
  - `stg_orders`: Order transaction data
- **Marts Layer**:
  - `customer_summary`: Aggregated customer metrics

## 🔄 Dagster+ Deployment

### GitHub Integration Setup

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial Dagster project setup"
   git push origin main
   ```

2. **Dagster+ Configuration**:
   - Create account at [dagster.cloud](https://dagster.cloud)
   - Connect your GitHub repository
   - Set up deployment configuration

3. **GitHub Secrets**:
   Add these secrets to your GitHub repository:
   ```
   DAGSTER_CLOUD_API_TOKEN: <your-dagster-cloud-token>
   ```

### Deployment Process

The project includes:
- **`dagster_cloud.yaml`**: Dagster+ deployment configuration
- **`.github/workflows/deploy.yml`**: GitHub Actions for CI/CD
- **`Dockerfile`**: Container configuration for deployment

## 🧪 Running the Pipeline

### Local Execution
1. Open Dagster UI at `http://localhost:3000`
2. Navigate to Assets
3. Select "Materialize All" to run the complete pipeline

### Production Execution
- Pipelines automatically deploy on push to `main` branch
- Schedule runs daily at 8 AM (configurable)
- Monitor execution in Dagster+ UI

## 📝 Development Workflow

### Adding New Assets
1. Define assets in `my_dagster_project/assets.py`
2. Update `definitions.py` if needed
3. Test locally with `dagster dev`
4. Push to GitHub for automatic deployment

### Adding New dbt Models
1. Create `.sql` files in `my_dagster_project/dbt_project/models/`
2. Update `dbt_project.yml` configuration if needed
3. Models are automatically included in Dagster assets

### Environment Variables
Configure these in Dagster+ for production:
```bash
SNOWFLAKE_ACCOUNT=PHWYUBU-GR70594
SNOWFLAKE_USER=KPAWAR9428
SNOWFLAKE_DATABASE=DBT_SNF
SNOWFLAKE_SCHEMA=DBT_SNF_SC
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
```

## 🔍 Monitoring & Debugging

### Local Development
- Dagster UI: `http://localhost:3000`
- Logs available in the UI
- Debug assets individually

### Production (Dagster+)
- Access via Dagster+ dashboard
- Real-time monitoring and alerting
- Asset lineage and dependency tracking

## 📚 Learning Resources

- [Dagster Documentation](https://docs.dagster.io/)
- [Dagster+ Deployment Guide](https://docs.dagster.io/dagster-plus/)
- [dbt Integration](https://docs.dagster.io/integrations/dbt)
- [Snowflake Integration](https://docs.dagster.io/integrations/snowflake)

## 🆘 Troubleshooting

### Common Issues
1. **Snowflake Authentication**: Ensure external browser authentication is enabled
2. **dbt Errors**: Check profiles.yml configuration
3. **Dependencies**: Run `pip install -e ".[dev]"` to install all requirements
4. **GitHub Actions**: Verify `DAGSTER_CLOUD_API_TOKEN` secret is set

### Support
- Check Dagster logs in the UI
- Review GitHub Actions logs for deployment issues
- Validate Snowflake connectivity with the test asset

## 🎯 Next Steps

1. **Customize Data Models**: Modify dbt models for your specific use case
2. **Add More Assets**: Create additional Dagster assets for your workflow
3. **Configure Monitoring**: Set up alerts and notifications in Dagster+
4. **Scale Infrastructure**: Adjust compute resources in Dagster+ settings

---

**Happy Data Engineering with Dagster! 🚀**
