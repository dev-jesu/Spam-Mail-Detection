# Contributing Guidelines

Thank you for your interest in contributing to the Spam Mail Detection System! 🎉

## 🤝 How to Contribute

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/spam-mail-detection.git
   cd spam-mail-detection
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Make your changes** and test them thoroughly
5. **Commit your changes**:
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Submit a Pull Request** on GitHub

## 📋 Pull Request Guidelines

- **Clear Title**: Use descriptive titles that explain what the PR does
- **Detailed Description**: Explain what changes were made and why
- **Link Issues**: Reference any related issues using `#issue_number`
- **Screenshots**: Include screenshots for UI changes
- **Testing**: Ensure all changes are tested and working

## 🐛 Bug Reports

When reporting bugs, please include:

- **Environment**: OS, Python version, Node.js version
- **Steps to reproduce**: Clear, numbered steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happened
- **Screenshots**: If applicable
- **Logs**: Any error messages or console output

## ✨ Feature Requests

We welcome new feature ideas! Include:

- **Problem**: What problem does this solve?
- **Solution**: How would you solve it?
- **Alternatives**: Other solutions you've considered
- **Additional context**: Any other relevant information

## 🧪 Development Setup

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## 📏 Code Style

### Python (Backend)
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and small

### JavaScript (Frontend)
- Use consistent indentation (2 spaces)
- Use meaningful variable and function names
- Follow React best practices
- Write JSDoc comments for complex functions

## 🧪 Testing

- **Backend**: Add unit tests for new functions
- **Frontend**: Test components and user interactions
- **Integration**: Test the full workflow when possible

## 📚 Documentation

- Update README.md for significant changes
- Add code comments for complex logic
- Update API documentation for backend changes

## 🏷️ Commit Message Format

Use meaningful commit messages:

- `feat: add new spam detection feature`
- `fix: resolve navbar spacing issue`
- `docs: update installation instructions`
- `refactor: clean up backend code structure`
- `test: add unit tests for prediction endpoint`

## ❓ Questions?

Feel free to ask questions by:

- Opening a [GitHub Issue](https://github.com/yourusername/spam-mail-detection/issues)
- Starting a [GitHub Discussion](https://github.com/yourusername/spam-mail-detection/discussions)

## 🤓 Code of Conduct

- Be respectful and inclusive
- Use welcoming and inclusive language
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- GitHub contributors page
- Release notes for significant contributions

Thank you for contributing to make spam detection better! 🚀
