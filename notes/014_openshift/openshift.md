---
title: OpenShift Onboarding
parent: Notes
nav_order: 14
description: "Onboarding an OpenShift cluster to AccuKnox — the Omni Operator, instance creation, secrets, and validation steps."
---

# OpenShift Cluster Onboarding Guide

## Prerequisites

Before starting the onboarding process, ensure the following requirements are met:

1. A **VolumeSnapshotClass** must be available in the cluster.
2. At least one VolumeSnapshotClass should be marked as the **default**.
3. All virtual machines to be scanned must use storage provided by the **same CSI driver**.
4. Run the required prerequisite validation script to confirm that the cluster is ready for onboarding.
5. Ensure you have cluster administrator permissions.

---

## 1. Install the AccuKnox Omni Operator

The AccuKnox Omni Operator is installed through the OpenShift OperatorHub by creating a custom CatalogSource.

### Create the CatalogSource

1. Log in to the OpenShift web console.

2. Navigate to:

   **Administration → Cluster Settings → OperatorHub**

3. Select **Create CatalogSource**.

4. Enter the container image URL provided by AccuKnox.

5. Configure the CatalogSource with **cluster-wide** visibility.

6. Create the CatalogSource.

After the CatalogSource is created successfully, the AccuKnox operator will become available under:

**Ecosystem → Software Catalog**

---

## 2. Install the Operator

1. Navigate to:

   **Ecosystem → Software Catalog**

2. Search for the **AccuKnox Omni Operator**.

3. Open the operator details page.

4. Select **Install**.

5. Choose the required installation namespace and approval strategy.

6. Complete the installation.

Verify that the operator installation is successful before proceeding.

---

## 3. Create an AccuKnox Instance

1. Navigate to:

   **Ecosystem → Installed Operators**

2. Select the **AccuKnox Omni Operator**.

3. Click **Create instance**.

4. Provide the following details:

   * **Name:** Enter a unique name for the AccuKnox instance.
   * **VM scanner label:** Specify the label used to identify the virtual machines that should be scanned.
   * Configure any additional settings supplied by AccuKnox.

5. Create the instance.

---

## 4. Create the Required Secret

1. Navigate to:

   **Workloads → Secrets**

2. Select the namespace in which the AccuKnox instance or operator is running.

3. Click **Create → Key/value secret** or use the YAML configuration provided by AccuKnox.

4. Enter the required credentials and configuration values.

5. Create the secret.

Record the exact **namespace** in which the secret was created. This namespace must be provided in the AccuKnox configuration wherever the secret reference is required.

---

## 5. Validate the Onboarding

After completing the installation:

1. Confirm that the AccuKnox Omni Operator is in the **Succeeded** state.
2. Verify that the AccuKnox custom resource instance has been created successfully.
3. Confirm that the required secret exists in the configured namespace.
4. Verify that the target virtual machines contain the expected VM scanner label.
5. Check the operator and scanner pod logs for any configuration or connectivity errors.
6. Confirm that the OpenShift cluster and its eligible virtual machines appear in the AccuKnox platform.
