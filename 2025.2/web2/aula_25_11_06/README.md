# CRUD no SQLAlchemy
As operações básicas de manipulação de dados em um banco são conhecidas como **CRUD**, sigla para:

**C**reate, **R**ead, **U**pdate, **D**elete.

No SQLAlchemy, cada uma dessas ações é feita com métodos Python que **substituem os comandos SQL tradicionais**.

### 🟢 **C — Create (Inserir dados)**

**Em SQL:**

```sql
INSERT INTO produto (nome, preco, quantidade)
VALUES ('Mouse', 79.90, 10);
```

**Em SQLAlchemy:**

```python
novo = Produto(nome="Mouse", preco=79.90, quantidade=10)
db.session.add(novo)
db.session.commit()
```

🧩 **Explicação:**

- `db.session.add()` → adiciona o objeto à “sessão” (como uma fila de alterações).
- `db.session.commit()` → confirma as alterações no banco, executando o `INSERT`.

---

### 🔵 **R — Read (Consultar dados)**

**Em SQL:**

```sql
SELECT * FROM produto;
```

**Em SQLAlchemy:**

```python
produtos = Produto.query.all()
```

**Ou filtrando (WHERE):**

```sql
SELECT * FROM produto WHERE id = 1;
```

**Em SQLAlchemy:**

```python
produto = Produto.query.get(1)
```

🧩 **Explicação:**

- `.query.all()` → retorna todos os registros da tabela.
- `.get(id)` → busca um registro pelo ID.

---

### 🟡 **U — Update (Atualizar dados)**

**Em SQL:**

```sql
UPDATE produto
SET preco = 89.90, quantidade = 15
WHERE id = 1;
```

**Em SQLAlchemy:**

```python
produto = Produto.query.get(1)
produto.preco = 89.90
produto.quantidade = 15
db.session.commit()
```

🧩 **Explicação:**

- Basta alterar os atributos do objeto Python.
- O `commit()` aplica essas mudanças no banco como um `UPDATE`.

---

### 🔴 **D — Delete (Excluir dados)**

**Em SQL:**

```sql
DELETE FROM produto WHERE id = 1;
```

**Em SQLAlchemy:**

```python
produto = Produto.query.get(1)
db.session.delete(produto)
db.session.commit()
```

🧩 **Explicação:**

- `db.session.delete()` marca o registro para exclusão.
- `db.session.commit()` executa o `DELETE` no banco.

---

### 🧮 **Resumo comparativo**

| Operação | Ação no SQLAlchemy | Comando SQL equivalente |
| --- | --- | --- |
| **Create** | `db.session.add()` + `commit()` | `INSERT INTO` |
| **Read** | `Produto.query.all()` / `.filter_by()` | `SELECT ... FROM` |
| **Update** | alterar atributos + `commit()` | `UPDATE ... SET` |
| **Delete** | `db.session.delete()` + `commit()` | `DELETE FROM` |

---