// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 查询 Domain 或 Drive 下文件数
 */
public class GetFileCountRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>drive_id</p>
     */
    @NameInMap("drive_id")
    @Validation(pattern = "[0-9]+")
    public String driveId;

    /**
     * <p>file_ext</p>
     */
    @NameInMap("file_ext")
    public String fileExt;

    /**
     * <p>subdomain</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static GetFileCountRequest build(java.util.Map<String, ?> map) throws Exception {
        GetFileCountRequest self = new GetFileCountRequest();
        return TeaModel.build(map, self);
    }

    public GetFileCountRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetFileCountRequest setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public GetFileCountRequest setFileExt(String fileExt) {
        this.fileExt = fileExt;
        return this;
    }
    public String getFileExt() {
        return this.fileExt;
    }

    public GetFileCountRequest setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}
