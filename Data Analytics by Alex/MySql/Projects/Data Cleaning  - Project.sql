-- Data Cleaning Project - Layoffs Data

-- Step 1: Create staging tables and import raw data
-- ==================================================

-- Create initial staging table
CREATE TABLE layoffs_staging LIKE layoffs;

-- Copy data to staging table
INSERT INTO layoffs_staging 
SELECT * FROM layoffs;

-- Create enhanced staging table with row numbers
CREATE TABLE layoffs_staging2 (
  `company` TEXT,
  `location` TEXT,
  `industry` TEXT,
  `total_laid_off` INT DEFAULT NULL,
  `percentage_laid_off` TEXT,
  `date` TEXT,
  `stage` TEXT,
  `country` TEXT,
  `funds_raised_millions` INT DEFAULT NULL,
  `row_num` INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Populate staging table with row numbers for duplicate detection
INSERT INTO layoffs_staging2
SELECT *,
  ROW_NUMBER() OVER(
    PARTITION BY company, location, industry, 
    total_laid_off, percentage_laid_off, `date`,
    stage, country, funds_raised_millions
  ) AS row_num
FROM layoffs_staging;

-- Step 2: Remove duplicates
-- ==========================
DELETE FROM layoffs_staging2 WHERE row_num > 1;

-- Step 3: Data standardization
-- =============================

-- Clean company names
UPDATE layoffs_staging2 SET company = TRIM(company);

-- Standardize crypto industry entries
UPDATE layoffs_staging2 
SET industry = 'Crypto' 
WHERE industry LIKE 'Crypto%';

-- Fix country name formatting
UPDATE layoffs_staging2 
SET country = TRIM(TRAILING '.' FROM country)
WHERE country LIKE 'United States%';

-- Convert date format
UPDATE layoffs_staging2 
SET `date` = STR_TO_DATE(`date`, '%m/%d/%Y');

-- Convert date column type
ALTER TABLE layoffs_staging2 
MODIFY COLUMN `date` DATE;

-- Step 4: Handle null/empty values
-- ================================

-- Set empty industry strings to NULL
UPDATE layoffs_staging2 
SET industry = NULL 
WHERE industry = '';

-- Populate missing industry values from matching companies
UPDATE layoffs_staging2 t1
JOIN layoffs_staging2 t2
  ON t1.company = t2.company
  AND t1.location = t2.location
SET t1.industry = t2.industry
WHERE t1.industry IS NULL 
  AND t2.industry IS NOT NULL;

-- Remove unusable records
DELETE FROM layoffs_staging2 
WHERE total_laid_off IS NULL 
  AND percentage_laid_off IS NULL;

-- Step 5: Final cleanup
-- ======================

-- Verify remaining data
SELECT * FROM layoffs_staging2;

-- Remove temporary row number column
ALTER TABLE layoffs_staging2 
DROP COLUMN row_num;

-- Final cleaned dataset
SELECT * FROM layoffs_staging2;
