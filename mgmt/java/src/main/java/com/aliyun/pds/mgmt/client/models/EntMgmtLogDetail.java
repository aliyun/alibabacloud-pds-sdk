// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class EntMgmtLogDetail extends TeaModel {
    @NameInMap("build_client")
    public DomainBuildClient buildClient;

    @NameInMap("domain_base_info")
    public DomainBaseInfoLogDetail domainBaseInfo;

    @NameInMap("domain_cname_info")
    public DomainCnameInfoLogDetail domainCnameInfo;

    @NameInMap("file_config")
    public DomainFileConfigDetail fileConfig;

    @NameInMap("file_custom_role_info")
    public FileCustomRoleInfoLogDetail fileCustomRoleInfo;

    @NameInMap("file_custom_role_info_updated_to")
    public FileCustomRoleInfoLogDetail fileCustomRoleInfoUpdatedTo;

    @NameInMap("multi_revision_config")
    public ExternalMultiFileRevisionConfig multiRevisionConfig;

    @NameInMap("senior_config")
    public DomainSeniorConfig seniorConfig;

    public static EntMgmtLogDetail build(java.util.Map<String, ?> map) throws Exception {
        EntMgmtLogDetail self = new EntMgmtLogDetail();
        return TeaModel.build(map, self);
    }

    public EntMgmtLogDetail setBuildClient(DomainBuildClient buildClient) {
        this.buildClient = buildClient;
        return this;
    }
    public DomainBuildClient getBuildClient() {
        return this.buildClient;
    }

    public EntMgmtLogDetail setDomainBaseInfo(DomainBaseInfoLogDetail domainBaseInfo) {
        this.domainBaseInfo = domainBaseInfo;
        return this;
    }
    public DomainBaseInfoLogDetail getDomainBaseInfo() {
        return this.domainBaseInfo;
    }

    public EntMgmtLogDetail setDomainCnameInfo(DomainCnameInfoLogDetail domainCnameInfo) {
        this.domainCnameInfo = domainCnameInfo;
        return this;
    }
    public DomainCnameInfoLogDetail getDomainCnameInfo() {
        return this.domainCnameInfo;
    }

    public EntMgmtLogDetail setFileConfig(DomainFileConfigDetail fileConfig) {
        this.fileConfig = fileConfig;
        return this;
    }
    public DomainFileConfigDetail getFileConfig() {
        return this.fileConfig;
    }

    public EntMgmtLogDetail setFileCustomRoleInfo(FileCustomRoleInfoLogDetail fileCustomRoleInfo) {
        this.fileCustomRoleInfo = fileCustomRoleInfo;
        return this;
    }
    public FileCustomRoleInfoLogDetail getFileCustomRoleInfo() {
        return this.fileCustomRoleInfo;
    }

    public EntMgmtLogDetail setFileCustomRoleInfoUpdatedTo(FileCustomRoleInfoLogDetail fileCustomRoleInfoUpdatedTo) {
        this.fileCustomRoleInfoUpdatedTo = fileCustomRoleInfoUpdatedTo;
        return this;
    }
    public FileCustomRoleInfoLogDetail getFileCustomRoleInfoUpdatedTo() {
        return this.fileCustomRoleInfoUpdatedTo;
    }

    public EntMgmtLogDetail setMultiRevisionConfig(ExternalMultiFileRevisionConfig multiRevisionConfig) {
        this.multiRevisionConfig = multiRevisionConfig;
        return this;
    }
    public ExternalMultiFileRevisionConfig getMultiRevisionConfig() {
        return this.multiRevisionConfig;
    }

    public EntMgmtLogDetail setSeniorConfig(DomainSeniorConfig seniorConfig) {
        this.seniorConfig = seniorConfig;
        return this;
    }
    public DomainSeniorConfig getSeniorConfig() {
        return this.seniorConfig;
    }

}
