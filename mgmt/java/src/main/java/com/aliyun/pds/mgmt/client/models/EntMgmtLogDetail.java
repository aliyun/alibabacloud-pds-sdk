// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class EntMgmtLogDetail extends TeaModel {
    @NameInMap("domain_base_info")
    public DomainBaseInfoLogDetail domainBaseInfo;

    @NameInMap("domain_cname_info")
    public DomainCnameInfoLogDetail domainCnameInfo;

    @NameInMap("file_custom_role_info")
    public FileCustomRoleInfoLogDetail fileCustomRoleInfo;

    @NameInMap("file_custom_role_info_updated_to")
    public FileCustomRoleInfoLogDetail fileCustomRoleInfoUpdatedTo;

    public static EntMgmtLogDetail build(java.util.Map<String, ?> map) throws Exception {
        EntMgmtLogDetail self = new EntMgmtLogDetail();
        return TeaModel.build(map, self);
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

}
