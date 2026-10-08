Commit Messages
===============

Valecraft follows the [Conventional Commits](https://www.conventionalcommits.org/) specification.

## Format

```text
<type>(<scope>): <description>
```

The `scope` is optional and identifies the part of the project affected by the change.

## Commit Types

| Type       | Description                                               | Example                                      |
| ---------- | --------------------------------------------------------- | -------------------------------------------- |
| `feat`     | Add a new feature                                         | `feat(player): add sprinting`                |
| `fix`      | Fix a bug                                                 | `fix(player): fix wall collision`            |
| `refactor` | Restructure code without changing behavior                | `refactor(scene): split level into scenes`   |
| `docs`     | Add or update documentation                               | `docs(readme): update installation guide`    |
| `style`    | Change formatting or code style without changing behavior | `style: format code with ruff`               |
| `perf`     | Improve performance                                       | `perf(rendering): optimize sprite rendering` |
| `build`    | Change build system or dependencies                       | `build: add pygame-ce dependency`            |
| `chore`    | Maintenance tasks that do not modify application behavior | `chore: update project metadata`             |
| `revert`   | Revert a previous commit                                  | `revert: revert player sprinting`            |

---

## Scopes

Scopes should identify the main area affected by the change.

Common scopes used in Valecraft:

| Scope     | Description                  |
| --------- | ---------------------------- |
| `game`    | Main game logic              |
| `display` | Window and display settings  |
| `player`  | Player system                |
| `scene`   | Scene management             |
| `level`   | Level system                 |
| `docs`    | Documentation                |
| `config`  | Project configuration        |