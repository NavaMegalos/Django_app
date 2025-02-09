
#### **Create `models.md`** (for documenting your models)

Create a new file `docs/brand_management/models.md`:

```markdown
# Models: Brand

The `Brand` model is used to represent a brand in the system. It has the following fields:

## Brand Model
```
```python
class Brand(models.Model):
    name = models.CharField(max_length=255)
```
