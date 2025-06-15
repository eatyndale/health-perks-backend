# Deploying to Railway

This guide will help you deploy the Health Perks API to Railway.app.

## Prerequisites

1. Create a Railway account at https://railway.app
2. Install Railway CLI:
```bash
# Using npm
npm i -g @railway/cli

# Using Homebrew (macOS)
brew install railway
```

## Deployment Steps

1. Login to Railway:
```bash
railway login
```

2. Initialize your project:
```bash
railway init
```

3. Link your project:
```bash
railway link
```

4. Set up environment variables:
```bash
railway variables set SECRET_KEY=your-secure-secret-key
railway variables set DATABASE_URL=your-database-url
railway variables set FRONTEND_URL=https://your-frontend-url.com
```

5. Deploy your application:
```bash
railway up
```

## Database Setup

Railway provides PostgreSQL databases. To use it:

1. Add PostgreSQL plugin in Railway dashboard
2. Get the connection URL from Railway dashboard
3. Set it as DATABASE_URL environment variable

## Environment Variables

Required environment variables:
- `SECRET_KEY`: Your application's secret key
- `DATABASE_URL`: Your database connection URL
- `FRONTEND_URL`: Your frontend application URL
- `PORT`: Railway will set this automatically

## Monitoring

Railway provides:
- Automatic HTTPS
- Built-in monitoring
- Logs viewer
- Metrics dashboard

## Custom Domains

1. Go to your project settings in Railway dashboard
2. Navigate to "Domains"
3. Add your custom domain
4. Follow the DNS configuration instructions

## Continuous Deployment

Railway automatically deploys when you push to your repository:

1. Connect your GitHub repository in Railway dashboard
2. Select the branch to deploy
3. Railway will automatically deploy on push

## Troubleshooting

Common issues and solutions:

1. Build fails:
   - Check requirements.txt
   - Verify Python version compatibility
   - Check build logs in Railway dashboard

2. Application crashes:
   - Check application logs
   - Verify environment variables
   - Check database connection

3. Database issues:
   - Verify DATABASE_URL
   - Check database logs
   - Ensure database migrations are applied

## Best Practices

1. Always use environment variables for sensitive data
2. Keep your dependencies updated
3. Monitor your application logs
4. Set up proper error handling
5. Use Railway's health checks
6. Implement proper logging
7. Set up proper CORS configuration
8. Use Railway's built-in monitoring

## Scaling

Railway automatically handles:
- Load balancing
- SSL/TLS
- CDN
- Auto-scaling

To manually scale:
1. Go to your project settings
2. Navigate to "Scaling"
3. Adjust the number of instances

## Backup and Recovery

1. Database backups:
   - Railway provides automatic PostgreSQL backups
   - Configure backup frequency in project settings

2. Application recovery:
   - Keep track of your deployments
   - Use Railway's rollback feature if needed
   - Maintain proper version control 