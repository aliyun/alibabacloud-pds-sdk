// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * ArchiveConfig 在线解压配置（可选配置，默认开启，未配置的role默认为AliyunPDSCloudUncompressRole）
 */
public class ArchiveConfig extends TeaModel {
    @NameInMap("archive_files_max_size")
    public Long archiveFilesMaxSize;

    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("role")
    public String role;

    @NameInMap("uncompress_file_max_size")
    public Long uncompressFileMaxSize;

    public static ArchiveConfig build(java.util.Map<String, ?> map) throws Exception {
        ArchiveConfig self = new ArchiveConfig();
        return TeaModel.build(map, self);
    }

    public ArchiveConfig setArchiveFilesMaxSize(Long archiveFilesMaxSize) {
        this.archiveFilesMaxSize = archiveFilesMaxSize;
        return this;
    }
    public Long getArchiveFilesMaxSize() {
        return this.archiveFilesMaxSize;
    }

    public ArchiveConfig setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public ArchiveConfig setRole(String role) {
        this.role = role;
        return this;
    }
    public String getRole() {
        return this.role;
    }

    public ArchiveConfig setUncompressFileMaxSize(Long uncompressFileMaxSize) {
        this.uncompressFileMaxSize = uncompressFileMaxSize;
        return this;
    }
    public Long getUncompressFileMaxSize() {
        return this.uncompressFileMaxSize;
    }

}
