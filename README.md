# freeduck

free duckdb GUI

## Pages

1. show tables
2. show one table

## Jump

1. select table and jump

### table raw data

```bash

  table_catalog: onething
  table_schema: main
  table_name: things
  table_type: BASE TABLE
  self_referencing_column_name: None
  reference_generation: None
  user_defined_type_catalog: None
  user_defined_type_schema: None
  user_defined_type_name: None
  is_insertable_into: YES
  is_typed: NO
  commit_action: None
  TABLE_COMMENT: None
--------------------------------------------------

```

show important keys

- table_name
- table_catalog
- table_type
- is_insertable_into
- is_typed

## SQL query

```sql
SELECT * FROM information_schema.tables WHERE table_name = 'things';
```
