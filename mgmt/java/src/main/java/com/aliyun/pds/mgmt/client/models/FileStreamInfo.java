// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FileStreamInfo extends TeaModel {
    /**
     * <p>content_hash</p>
     */
    @NameInMap("content_hash")
    public String contentHash;

    /**
     * <p>content_hash_name</p>
     */
    @NameInMap("content_hash_name")
    public String contentHashName;

    /**
     * <p>ContentMd5</p>
     */
    @NameInMap("content_md5")
    @Validation(required = true)
    public String contentMd5;

    /**
     * <p>part_info_list</p>
     */
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    /**
     * <p>pre_hash</p>
     */
    @NameInMap("pre_hash")
    public String preHash;

    /**
     * <p>proof_code</p>
     */
    @NameInMap("proof_code")
    public String proofCode;

    /**
     * <p>proof_version</p>
     */
    @NameInMap("proof_version")
    public String proofVersion;

    /**
     * <p>Size</p>
     */
    @NameInMap("size")
    @Validation(required = true)
    public Long size;

    public static FileStreamInfo build(java.util.Map<String, ?> map) throws Exception {
        FileStreamInfo self = new FileStreamInfo();
        return TeaModel.build(map, self);
    }

    public FileStreamInfo setContentHash(String contentHash) {
        this.contentHash = contentHash;
        return this;
    }
    public String getContentHash() {
        return this.contentHash;
    }

    public FileStreamInfo setContentHashName(String contentHashName) {
        this.contentHashName = contentHashName;
        return this;
    }
    public String getContentHashName() {
        return this.contentHashName;
    }

    public FileStreamInfo setContentMd5(String contentMd5) {
        this.contentMd5 = contentMd5;
        return this;
    }
    public String getContentMd5() {
        return this.contentMd5;
    }

    public FileStreamInfo setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public FileStreamInfo setPreHash(String preHash) {
        this.preHash = preHash;
        return this;
    }
    public String getPreHash() {
        return this.preHash;
    }

    public FileStreamInfo setProofCode(String proofCode) {
        this.proofCode = proofCode;
        return this;
    }
    public String getProofCode() {
        return this.proofCode;
    }

    public FileStreamInfo setProofVersion(String proofVersion) {
        this.proofVersion = proofVersion;
        return this;
    }
    public String getProofVersion() {
        return this.proofVersion;
    }

    public FileStreamInfo setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

}
