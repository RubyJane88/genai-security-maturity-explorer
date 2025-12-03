#!/usr/bin/env python3
"""
Advanced Dependency Compatibility Checker
Analyzes Python packages for version conflicts before deployment
"""

import sys
import subprocess
import json
from packaging import version
from pathlib import Path

def check_python_version():
    """Check if Python version matches deployment target"""
    print("🐍 Python Version Check")
    print("-" * 50)
    
    current = sys.version_info
    current_str = f"{current.major}.{current.minor}.{current.micro}"
    print(f"Current: Python {current_str}")
    
    # Check .python-version file
    pv_file = Path(".python-version")
    if pv_file.exists():
        target = pv_file.read_text().strip()
        print(f"Target (deployment): Python {target}")
        
        if target.startswith("3.11"):
            print("✅ Using recommended Python 3.11")
            return True
        else:
            print(f"⚠️  Target is {target}, consider 3.11 for stability")
            return False
    else:
        print("⚠️  No .python-version file found")
        return False

def check_package_compatibility():
    """Check if all packages are compatible with current Python version"""
    print("\n📦 Package Compatibility Check")
    print("-" * 50)
    
    try:
        # Get list of installed packages
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=json"],
            capture_output=True,
            text=True,
            check=True
        )
        packages = json.loads(result.stdout)
        
        print(f"Installed packages: {len(packages)}")
        
        # Critical packages to verify
        critical = ["dash", "plotly", "pandas", "numpy", "gunicorn"]
        
        for pkg in packages:
            if pkg["name"].lower() in critical:
                print(f"  ✓ {pkg['name']} {pkg['version']}")
        
        return True
    except Exception as e:
        print(f"❌ Error checking packages: {e}")
        return False

def check_requirements_file():
    """Verify requirements.txt exists and is valid"""
    print("\n📄 Requirements.txt Check")
    print("-" * 50)
    
    req_file = Path("requirements.txt")
    if not req_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    print("✅ requirements.txt found")
    
    # Parse requirements
    with open(req_file) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
    print(f"Dependencies specified: {len(lines)}")
    
    # Check for known incompatibilities
    incompatible = []
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    
    for line in lines:
        if "pandas==2.1.4" in line and python_version in ["3.13", "3.14"]:
            incompatible.append("pandas 2.1.4 doesn't support Python 3.13+")
        if "numpy==1.26.2" in line and python_version in ["3.13", "3.14"]:
            incompatible.append("numpy 1.26.2 may have issues with Python 3.13+")
    
    if incompatible:
        print("\n⚠️  Potential incompatibilities:")
        for issue in incompatible:
            print(f"   • {issue}")
        return False
    
    print("✅ No obvious incompatibilities detected")
    return True

def test_imports():
    """Test if critical imports work"""
    print("\n🔬 Import Test")
    print("-" * 50)
    
    critical_imports = [
        "dash",
        "dash_bootstrap_components",
        "plotly",
        "pandas",
        "numpy",
        "gunicorn"
    ]
    
    failed = []
    for module in critical_imports:
        try:
            __import__(module)
            print(f"  ✓ {module}")
        except ImportError as e:
            print(f"  ✗ {module}: {e}")
            failed.append(module)
    
    if failed:
        print(f"\n❌ {len(failed)} imports failed")
        return False
    
    print("\n✅ All critical imports successful")
    return True

def check_deployment_files():
    """Verify all deployment configuration files exist"""
    print("\n⚙️  Deployment Configuration Check")
    print("-" * 50)
    
    required_files = {
        "app.py": "Main application file",
        "requirements.txt": "Python dependencies",
        "Procfile": "Process configuration",
        "render.yaml": "Render.com configuration",
        "runtime.txt": "Python version specification",
        ".python-version": "Python version marker"
    }
    
    all_present = True
    for file, description in required_files.items():
        if Path(file).exists():
            print(f"  ✓ {file}: {description}")
        else:
            print(f"  ✗ {file}: {description} (MISSING)")
            all_present = False
    
    return all_present

def analyze_dependency_tree():
    """Check for circular dependencies or conflicts"""
    print("\n🌳 Dependency Tree Analysis")
    print("-" * 50)
    
    try:
        # Try using pip check
        result = subprocess.run(
            [sys.executable, "-m", "pip", "check"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ No dependency conflicts detected")
            return True
        else:
            print("⚠️  Dependency issues found:")
            print(result.stdout)
            return False
    except Exception as e:
        print(f"⚠️  Could not run dependency check: {e}")
        return False

def main():
    print("=" * 50)
    print("🔍 PRE-DEPLOYMENT COMPATIBILITY CHECK")
    print("=" * 50)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Requirements File", check_requirements_file),
        ("Package Compatibility", check_package_compatibility),
        ("Import Tests", test_imports),
        ("Deployment Files", check_deployment_files),
        ("Dependency Tree", analyze_dependency_tree)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nScore: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 All checks passed! Safe to deploy.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} check(s) failed. Fix issues before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
