# AWS Day 1 & Day 2 — Table of Contents

## Summary

This file is a day-wise table of contents for the AWS Day-1 and Day-2 study notes.  
It includes quick summaries, topic links, hands-on practice links, and revision links.

---

## Day-Wise Table of Contents

| Day | Main Topic | Summary | Study Notes Links |
|---|---|---|---|
| Day 1 | AWS Cloud Foundations | Covers how to start learning AWS, cloud computing basics, core AWS services, AWS benefits, global infrastructure, shared responsibility model, AWS account setup, billing basics, root user vs IAM user, MFA, and Well-Architected 6 Pillars. | [Learning Path](#1-how-would-i-start-learning-aws-cloud) <br> [Do I Need 200+ Services?](#2-do-i-need-to-learn-200-aws-services) <br> [Cloud Computing](#3-what-is-cloud-computing) <br> [Cloud Service Models](#4-cloud-service-models) <br> [Why AWS?](#5-why-aws) <br> [Benefits](#6-benefits-at-a-glance) <br> [Global Infrastructure](#7-aws-global-infrastructure) <br> [Shared Responsibility](#8-shared-responsibility-model) <br> [AWS Account Setup](#9-why-set-up-an-aws-account) <br> [Billing Basics](#11-aws-billing-basics) <br> [Root User vs IAM User + MFA](#12-root-user-vs-iam-user--mfa) <br> [Well-Architected Pillars](#13-aws-well-architected-6-pillars) |
| Day 2 | IAM Users, Groups, Roles & Policies | Covers IAM basics, authentication vs authorization, why IAM matters, IAM users, groups, roles, policies, managed policies, inline policies, JSON policy structure, least privilege, permission boundaries, and IAM best practices. | [What is IAM?](#1-what-is-iam) <br> [Authentication vs Authorization](#2-authentication-vs-authorization) <br> [Why IAM Matters](#3-why-iam-matters) <br> [IAM Core Concepts](#4-iam-core-concepts) <br> [IAM Roles](#5-iam-roles) <br> [IAM Policies](#6-iam-policies) <br> [Types of IAM Policies](#7-types-of-iam-policies) <br> [Managed vs Inline Policy](#8-managed-policy-vs-inline-policy) <br> [JSON Policy Structure](#9-json-policy-structure) <br> [Least Privilege](#10-least-privilege) <br> [Permission Boundaries](#11-permission-boundaries) <br> [IAM Best Practices](#12-iam-best-practices) |

---

## Quick Revision Table

| Section | Purpose | Link |
|---|---|---|
| Important One-Line Definitions | Fast revision of important AWS and IAM terms | [Quick Revision](#day-1--day-2-quick-revision) |
| Common Interview Questions | Interview-style AWS and IAM questions with answers | [Interview Questions](#common-interview-style-questions) |
| Hands-On Practice Ideas | Practical labs for Day 1 and Day 2 | [Hands-On Practice](#hands-on-practice-ideas) |
| Final Summary | Final short recap of both days | [Final Summary](#final-summary) |

---

## Day 1 Short Summary

Day 1 builds the AWS foundation. It explains what cloud computing is, why AWS is used, how AWS global infrastructure works, what the shared responsibility model means, how to set up and secure an AWS account, how billing works, why MFA is important, and what the AWS Well-Architected 6 Pillars are.

### Day 1 Key Takeaways

| Topic | Key Point |
|---|---|
| AWS Learning Path | Start with basics, security, core services, and hands-on labs |
| Cloud Computing | On-demand IT resources over the internet |
| Core AWS Services | Learn IAM, EC2, S3, VPC, RDS, CloudWatch, and Lambda first |
| AWS Global Infrastructure | Regions, Availability Zones, Edge Locations, Local Zones, and Wavelength Zones |
| Shared Responsibility | AWS secures the cloud; customer secures what they create in the cloud |
| Billing | Use budgets, alerts, and delete unused resources |
| Root User | Protect with MFA and avoid daily use |
| Well-Architected | Design systems with security, reliability, performance, cost, operations, and sustainability in mind |

---

## Day 2 Short Summary

Day 2 focuses on IAM security. It explains how AWS controls identity and permissions using IAM users, groups, roles, and policies. It also explains authentication, authorization, least privilege, JSON policy structure, managed policies, inline policies, permission boundaries, and IAM best practices.

### Day 2 Key Takeaways

| Topic | Key Point |
|---|---|
| IAM | Identity and Access Management controls access to AWS resources |
| Authentication | Who are you? |
| Authorization | What are you allowed to do? |
| IAM User | Named identity for a person or workload |
| IAM Group | Collection of IAM users with common permissions |
| IAM Role | Temporary permissions for trusted entities like EC2 or Lambda |
| IAM Policy | JSON document that allows or denies actions |
| Least Privilege | Give only the permissions required |
| Permission Boundary | Sets the maximum permissions an identity can have |
| IAM Best Practice | Use MFA, roles, groups, and review permissions regularly |

---

## Recommended Study Flow

| Step | What to Study | Reason |
|---|---|---|
| 1 | Day 1 cloud basics | Build foundation before IAM |
| 2 | AWS account setup and billing | Learn safe account usage |
| 3 | Shared Responsibility Model | Understand security ownership |
| 4 | Root user, IAM user, and MFA | Secure the account properly |
| 5 | Day 2 IAM basics | Learn access control |
| 6 | IAM roles and policies | Understand real-world AWS permissions |
| 7 | Least privilege and permission boundaries | Learn secure permission design |
| 8 | Hands-on practice | Convert theory into real skill |

---

## Files in This Study Package

| File | Purpose |
|---|---|
| `AWS-Day-1-and-Day-2-Combined.pptx` | Combined PowerPoint slides for Day 1 and Day 2 |
| `AWS-Day-1-and-Day-2-Study-Notes.md` | Full study notes |
| `aws-day-1-day-2-mcqs-quiz.html` | Interactive MCQs quiz with timer, score, answer checking, explanations, and answer shuffle |
| `AWS-Day-1-and-Day-2-TOC.md` | This table of contents and summary file |

---

## Final Revision Line

**Day 1 = AWS foundation**  
**Day 2 = AWS IAM security**

Most important mindset:

**Secure first, practice hands-on, and always use least privilege.**


---

# Full Study Notes

# Day 1 — AWS Cloud Foundations

## 1. How Would I Start Learning AWS Cloud?

A good AWS learning path should begin with the basics, not with trying to memorize every AWS service.

### Recommended learning order

1. **Cloud fundamentals first**
   - Understand what cloud computing means.
   - Learn why companies use cloud instead of only physical data centers.

2. **AWS account and security foundation**
   - Learn how to create an AWS account safely.
   - Secure the root user.
   - Enable MFA.
   - Create IAM users or roles for daily work.

3. **Core services, not 200+ services**
   - Focus first on services used in most real projects.
   - Examples:
     - EC2
     - S3
     - IAM
     - VPC
     - RDS
     - CloudWatch
     - Lambda

4. **Hands-on practice from Day 1**
   - Do not only watch videos.
   - Create small labs.
   - Practice using the AWS Console and AWS CLI.

5. **Real architecture mindset**
   - Think like an engineer.
   - Ask:
     - Why am I using this service?
     - How does traffic flow?
     - How is it secured?
     - How will I monitor it?
     - How will I control cost?

6. **Exam scenarios + project confidence**
   - AWS exams often test real-life scenarios.
   - Hands-on practice helps with both certification and job interviews.

---

## 2. Do I Need to Learn 200+ AWS Services?

No. You do not need to learn every AWS service at the beginning.

AWS has many services, but most beginners should start with the services that appear in real projects and certifications again and again.

### Focus areas first

| Area | Services to learn first | Why it matters |
|---|---|---|
| Compute | EC2, Lambda | Run applications and workloads |
| Storage | S3, EBS | Store files, objects, and disk data |
| Networking | VPC, Subnets, Security Groups | Control communication and access |
| Identity & Security | IAM, MFA, Policies | Secure users and resources |
| Database | RDS, DynamoDB basics | Store application data |
| Monitoring | CloudWatch | Track logs, metrics, and alarms |
| Billing | Billing Dashboard, Budgets | Avoid surprise charges |

### Simple rule

Learn the services that help you build a real project first. After that, expand slowly.

---

## 3. What is Cloud Computing?

Cloud computing means using IT resources over the internet instead of buying and maintaining all physical infrastructure yourself.

AWS describes cloud computing as the **on-demand delivery of IT resources over the internet with pay-as-you-go pricing**.

### Key ideas

| Concept | Meaning |
|---|---|
| On-demand | You can create resources when needed |
| Internet-based | Services are accessed online |
| Pay-as-you-go | You pay for what you use |
| Scalable | You can increase or decrease resources |
| Managed services | AWS handles many backend tasks |

---

## 4. Cloud Service Models

Cloud services are commonly divided into three main models:

## IaaS — Infrastructure as a Service

IaaS gives you basic infrastructure like servers, networking, and storage.

### Example

- **Amazon EC2**

### You manage

- Operating system
- Applications
- Security configuration
- Updates and patches

### AWS manages

- Physical servers
- Data centers
- Hardware
- Networking infrastructure

---

## PaaS — Platform as a Service

PaaS gives you a platform to deploy code without managing the full server infrastructure.

### Example

- **AWS Lambda**

### You manage

- Code
- Application logic
- Permissions
- Configuration

### AWS manages

- Servers
- Runtime environment
- Scaling infrastructure

---

## SaaS — Software as a Service

SaaS is a complete software application delivered over the internet.

### Example

- **Amazon QuickSight**

### You manage

- User access
- Data usage
- Application settings

### Provider manages

- Application hosting
- Updates
- Infrastructure
- Maintenance

---

## 5. Why AWS?

AWS is one of the leading cloud providers worldwide.

### Reasons companies use AWS

1. **Large global presence**
   - AWS has many regions and availability zones.

2. **Many services**
   - AWS provides services for compute, storage, databases, networking, security, analytics, AI, DevOps, and more.

3. **Trusted by many customers**
   - Startups, enterprises, government organizations, and educational institutions use AWS.

4. **Flexible**
   - You can start small and scale later.

5. **Cost-effective**
   - Pay only for what you use.

6. **Secure**
   - AWS provides many tools for identity, encryption, logging, monitoring, and compliance.

---

## 6. Benefits at a Glance

| Benefit | Explanation |
|---|---|
| Easy to use | AWS Console and CLI make resource management easier |
| Flexible | Many service options for different needs |
| Cost-effective | Pay-as-you-go model helps reduce upfront costs |
| Reliable | Built for high availability and fault tolerance |
| Scalable | Increase or decrease capacity when needed |
| Secure | Security tools like IAM, MFA, encryption, and logging |

---

## 7. AWS Global Infrastructure

AWS global infrastructure is the worldwide system of regions, availability zones, edge locations, and other infrastructure components used to run AWS services.

### Important terms

| Term | Meaning |
|---|---|
| Region | A geographic area where AWS has data centers |
| Availability Zone | One or more separate data centers inside a region |
| Edge Location | Location used to deliver content closer to users |
| Local Zone | AWS infrastructure closer to large cities or users |
| Wavelength Zone | AWS infrastructure designed for ultra-low-latency 5G applications |

### Why global infrastructure matters

- Improves availability
- Reduces latency
- Supports disaster recovery
- Helps serve users closer to their location
- Allows architecture across multiple regions or zones

---

## 8. Shared Responsibility Model

AWS security is shared between **AWS** and the **customer**.

### Main idea

- AWS is responsible for **security OF the cloud**.
- Customer is responsible for **security IN the cloud**.

---

## AWS Responsibility — Security OF the Cloud

AWS manages and protects the infrastructure that runs AWS services.

### AWS is responsible for

- Physical data centers
- Hardware
- Networking infrastructure
- Storage infrastructure
- Global infrastructure
- Managed service backend infrastructure

---

## Customer Responsibility — Security IN the Cloud

The customer is responsible for how they configure and use AWS services.

### Customer is responsible for

- IAM users, roles, and permissions
- Data security
- Application security
- Network access rules
- Operating system patching for EC2
- Encryption configuration
- Backups
- Monitoring and logging

---

## Responsibility depends on service type

| Service Type | Example | Customer responsibility level |
|---|---|---|
| IaaS | EC2 | More responsibility |
| PaaS | Lambda | Medium responsibility |
| SaaS | QuickSight | Less responsibility |

### Example

With **EC2**, you manage the operating system and patches.  
With **Lambda**, AWS manages the server infrastructure, and you focus more on code and permissions.

---

## 9. Why Set Up an AWS Account?

You need an AWS account to practice real AWS services.

### Reasons to set up an account

1. Hands-on practice with real AWS services
2. Access to Free Tier and selected free services
3. Build projects and gain practical experience
4. Prepare for AWS certification exams
5. Learn real cloud architecture

---

## 10. Setting Up Your AWS Account

### Basic steps

1. Visit the AWS website and create an AWS account.
2. Enter email, password, and account name.
3. Add contact information.
4. Add payment method.
5. Verify phone number.
6. Review support options.
7. Complete sign-up.
8. Secure the account immediately.

### After account creation

Do these security steps first:

1. Enable MFA on the root user.
2. Create an IAM user or use IAM Identity Center for daily work.
3. Do not use the root user for regular tasks.
4. Set billing alerts or budgets.
5. Review account security settings.

---

## 11. AWS Billing Basics

AWS uses a pay-as-you-go model.

### Important billing practices

| Practice | Why it matters |
|---|---|
| Pay only for what you use | Helps avoid large upfront cost |
| Use Free Tier carefully | Some services are free only within limits |
| Set billing alerts | Helps track spending |
| Check Billing Dashboard regularly | Helps catch unexpected charges |
| Stop or delete unused resources | Prevents unnecessary cost |

### Beginner warning

Always delete resources after practice labs if you no longer need them.

Common resources that may cost money:

- EC2 instances
- EBS volumes
- NAT Gateway
- Load Balancers
- RDS databases
- Elastic IPs if unused
- Large S3 storage

---

## 12. Root User vs IAM User + MFA

## Root User

The root user is the main account owner identity created when the AWS account is created.

### Root user has

- Full access to everything
- Account-level permissions
- Billing and account control

### Best practice

Do not use the root user for daily work.

Use root only for account-level tasks.

---

## IAM User

An IAM user is an identity created inside AWS IAM.

### IAM user is used for

- Daily administrative work
- Developer access
- Limited permissions
- Console or CLI access

### Best practice

Give IAM users only the permissions they need.

---

## MFA — Multi-Factor Authentication

MFA adds an extra security layer.

Instead of only using a password, MFA requires another verification method.

### Why MFA is important

- Protects against stolen passwords
- Adds extra account security
- Strongly recommended for root user and admin users

### Best practice

Enable MFA immediately on the root user.

---

## 13. AWS Well-Architected 6 Pillars

The AWS Well-Architected Framework helps design secure, reliable, efficient, and cost-effective cloud systems.

### 6 pillars

| Pillar | Meaning |
|---|---|
| Operational Excellence | Run and monitor systems effectively |
| Security | Protect data, systems, and assets |
| Reliability | Recover from failures and keep systems running |
| Performance Efficiency | Use resources efficiently |
| Cost Optimization | Avoid unnecessary cost |
| Sustainability | Reduce environmental impact and improve efficiency |

---

# Day 2 — IAM Users, Groups, Roles & Policies

## 1. What is IAM?

IAM stands for **Identity and Access Management**.

IAM is an AWS service used to control access to AWS resources.

### IAM helps answer two questions

| Question | Concept |
|---|---|
| Who are you? | Authentication |
| What are you allowed to do? | Authorization |

---

## 2. Authentication vs Authorization

## Authentication

Authentication means verifying identity.

### Simple meaning

**Authentication = Who are you?**

### Examples

- Username and password
- MFA code
- Access key and secret key
- Identity provider login

---

## Authorization

Authorization means checking permissions after identity is verified.

### Simple meaning

**Authorization = What are you allowed to do?**

### Examples

- Can this user list S3 buckets?
- Can this role start EC2 instances?
- Can this group access billing?
- Can this Lambda function write logs?

---

## 3. Why IAM Matters

IAM is very important because it controls access to AWS resources.

### If IAM is weak

- Unauthorized users may access resources.
- Data may be exposed.
- Production systems may be changed or deleted.
- Attackers may create expensive resources.
- Automation may fail or become insecure.

### IAM controls

1. Who can sign in
2. What actions are allowed
3. Which resources can be accessed
4. Secure automation using roles
5. Access for users, groups, and workloads

---

## 4. IAM Core Concepts

IAM uses identities and permissions to control access.

### Main formula

**Identity + Permissions = Access**

---

## Root User

The root user is the AWS account owner identity.

### Important points

- Created when the AWS account is created
- Has full access to the account
- Should not be used for daily work
- Should have MFA enabled

---

## IAM User

An IAM user is a named identity for a person or workload that needs AWS access.

### Example

- Admin user
- Developer user
- Read-only user
- Automation user

---

## IAM Group

An IAM group is a collection of IAM users with common permissions.

### Example

Instead of assigning the same policy to many users one by one, create a group.

| Group | Example permissions |
|---|---|
| Admins | Full admin access |
| Developers | EC2, S3, CloudWatch limited access |
| ReadOnly | View-only access |
| Billing | Billing dashboard access |

### Important point

Groups make permission management easier.

---

## IAM Role

An IAM role provides temporary permissions.

Roles are assumed by trusted entities.

### Used by

- EC2
- Lambda
- AWS services
- Cross-account users
- Federated users
- Applications

### Important point

IAM roles use temporary credentials, often issued through AWS STS.

---

## IAM Policy

An IAM policy is a JSON document that defines allowed or denied actions.

### Policy controls

- What actions are allowed
- What actions are denied
- Which resources are affected
- Optional conditions for access

---

## 5. IAM Roles

IAM roles are very important for secure AWS automation.

### Key points

1. Roles are assumed by trusted entities.
2. Roles are used by EC2, Lambda, and cross-account users.
3. Temporary credentials are issued by AWS STS.
4. Roles are best for services that need AWS access.
5. Example role name: `EC2S3ReadOnlyRole`

---

## Role example

### Scenario

An EC2 instance needs to read files from an S3 bucket.

### Bad practice

Store access keys directly inside the EC2 instance.

### Good practice

Attach an IAM role to the EC2 instance with S3 read-only permission.

### Why?

- No long-term access keys stored on the server
- Temporary credentials are used
- Easier to rotate and manage
- More secure

---

## 6. IAM Policies

A policy defines permissions.

### Simple meaning

**Policy = Allow or Deny actions on resources**

### Example permission logic

- Allow user to read S3 bucket
- Deny deleting EC2 instances
- Allow Lambda to write CloudWatch logs
- Allow admin group to manage IAM

---

## 7. Types of IAM Policies

## AWS Managed Policy

AWS managed policies are created and maintained by AWS.

### Example

- `AmazonS3ReadOnlyAccess`

### Good for

- Quick setup
- Common permission needs
- Beginner learning

### Limitation

They may be broader than needed for production.

---

## Customer Managed Policy

Customer managed policies are created and managed by you.

### Good for

- Reusable permissions
- Custom access control
- Better least privilege
- Attaching to multiple users, groups, or roles

### Example

Create a custom policy that allows only reading one specific S3 bucket.

---

## Inline Policy

An inline policy is embedded directly into one user, group, or role.

### Good for

- One-to-one permission relationship
- Special case permissions

### Limitation

Less reusable and harder to manage at scale.

---

## 8. Managed Policy vs Inline Policy

| Feature | Managed Policy | Inline Policy |
|---|---|---|
| Reusable | Yes | No |
| Attached to multiple identities | Yes | No |
| Easier to manage | Yes | Usually no |
| Best for | Common permissions | Special one-identity permission |
| Created by | AWS or customer | Customer |
| Deleted with identity | No, unless manually deleted | Yes, tied to identity |

---

## 9. JSON Policy Structure

IAM policies are written in JSON.

### Common policy elements

| Element | Meaning |
|---|---|
| Version | Policy language version |
| Statement | Main permission block |
| Effect | Allow or Deny |
| Action | AWS API action |
| Resource | AWS resource affected |
| Condition | Optional rule for when permission applies |

### Basic policy example

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example-bucket"
    }
  ]
}
```

### Explanation

| Line | Meaning |
|---|---|
| Version | Uses current AWS policy language version |
| Effect | Allows the action |
| Action | Allows listing an S3 bucket |
| Resource | Applies only to one bucket |

---

## 10. Least Privilege

Least privilege means giving only the permissions required to do the job.

### Simple meaning

Do not give extra permissions.

### Example

If a user only needs to read S3 files, do not give full S3 access.

### Bad permission

```json
"Action": "s3:*"
```

### Better permission

```json
"Action": [
  "s3:GetObject",
  "s3:ListBucket"
]
```

---

## 11. Permission Boundaries

A permission boundary sets the maximum permissions an IAM user or role can have.

### Simple meaning

Even if a policy allows something, the permission boundary can limit it.

### Why permission boundaries matter

- Prevent privilege escalation
- Control maximum access
- Useful in large teams
- Useful when developers can create roles or users

---

## 12. IAM Best Practices

| Best Practice | Why |
|---|---|
| Enable MFA on root user | Protects the main account |
| Do not use root for daily work | Reduces risk |
| Use IAM users or Identity Center for people | Better access control |
| Use roles for AWS services | Avoids long-term credentials |
| Follow least privilege | Reduces damage if credentials are compromised |
| Use groups for users | Easier permission management |
| Review permissions regularly | Removes unnecessary access |
| Avoid hardcoding access keys | Protects credentials |
| Use managed policies carefully | Some policies may be too broad |
| Prefer customer managed policies for custom needs | Better control |

---

# Day 1 + Day 2 Quick Revision

## Important one-line definitions

| Term | Definition |
|---|---|
| Cloud Computing | On-demand IT resources over the internet |
| AWS | Amazon cloud platform |
| Region | Geographic AWS location |
| Availability Zone | Isolated data center area inside a region |
| Edge Location | Location used for faster content delivery |
| Shared Responsibility Model | Security is shared between AWS and customer |
| Root User | Main AWS account owner identity |
| IAM User | Named identity for a person or workload |
| IAM Group | Collection of users with common permissions |
| IAM Role | Temporary permissions for trusted entities |
| IAM Policy | JSON document that allows or denies actions |
| Authentication | Verifies who you are |
| Authorization | Checks what you can do |
| MFA | Extra verification layer |
| Least Privilege | Give only required permissions |
| Permission Boundary | Maximum permission limit |

---

# Common Interview-Style Questions

## Q1. What is cloud computing?

Cloud computing is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing.

---

## Q2. Do beginners need to learn all AWS services?

No. Beginners should focus on core services first, such as IAM, EC2, S3, VPC, RDS, CloudWatch, and Lambda.

---

## Q3. What is the AWS Shared Responsibility Model?

It means AWS is responsible for security of the cloud, while the customer is responsible for security in the cloud.

---

## Q4. What is the difference between root user and IAM user?

The root user is the main account owner with full access. An IAM user is created for daily work and can have limited permissions.

---

## Q5. Why should MFA be enabled?

MFA adds an extra security layer and protects the account even if the password is stolen.

---

## Q6. What is IAM?

IAM is Identity and Access Management. It controls who can access AWS resources and what actions they can perform.

---

## Q7. Authentication vs authorization?

Authentication verifies identity. Authorization checks permissions.

---

## Q8. What is an IAM role?

An IAM role is an identity with temporary permissions that can be assumed by trusted entities like EC2, Lambda, or cross-account users.

---

## Q9. What is an IAM policy?

An IAM policy is a JSON document that defines allowed or denied actions on AWS resources.

---

## Q10. What is least privilege?

Least privilege means giving only the permissions required to perform a task and nothing extra.

---

# Hands-On Practice Ideas

## Day 1 practice

1. Create an AWS account.
2. Enable MFA on root user.
3. Open Billing Dashboard.
4. Create a budget alert.
5. Explore AWS regions.
6. Learn the difference between EC2, S3, IAM, VPC, and CloudWatch.

## Day 2 practice

1. Create an IAM user.
2. Create an IAM group.
3. Attach a read-only policy to the group.
4. Add user to the group.
5. Create an IAM role for EC2.
6. Attach an S3 read-only policy to the role.
7. Review JSON policy structure.
8. Practice least privilege.

---

# Final Summary

Day 1 builds the foundation of AWS Cloud:

- What cloud computing is
- Why AWS is used
- AWS global infrastructure
- Shared responsibility model
- AWS account setup
- Billing basics
- Root user, IAM user, and MFA
- AWS Well-Architected pillars

Day 2 focuses on IAM security:

- Authentication and authorization
- IAM users, groups, roles, and policies
- Managed and inline policies
- JSON policy structure
- Least privilege
- Permission boundaries
- IAM best practices

The most important mindset is:

**Secure first, practice hands-on, and always use least privilege.**
