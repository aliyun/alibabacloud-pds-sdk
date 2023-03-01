// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainFileConfigDetail extends TeaModel {
    @NameInMap("allow_upload_custom_file_ext_list")
    public java.util.List<String> allowUploadCustomFileExtList;

    @NameInMap("allow_upload_file_category_list")
    public java.util.List<String> allowUploadFileCategoryList;

    @NameInMap("recycle_bin_auto_delete_enabled")
    public Boolean recycleBinAutoDeleteEnabled;

    @NameInMap("recycle_bin_auto_delete_keep_second")
    public Long recycleBinAutoDeleteKeepSecond;

    @NameInMap("same_name_file_upload_mode")
    public String sameNameFileUploadMode;

    @NameInMap("single_file_upload_size_limit")
    public Long singleFileUploadSizeLimit;

    @NameInMap("web_client_download_mode")
    public String webClientDownloadMode;

    public static DomainFileConfigDetail build(java.util.Map<String, ?> map) throws Exception {
        DomainFileConfigDetail self = new DomainFileConfigDetail();
        return TeaModel.build(map, self);
    }

    public DomainFileConfigDetail setAllowUploadCustomFileExtList(java.util.List<String> allowUploadCustomFileExtList) {
        this.allowUploadCustomFileExtList = allowUploadCustomFileExtList;
        return this;
    }
    public java.util.List<String> getAllowUploadCustomFileExtList() {
        return this.allowUploadCustomFileExtList;
    }

    public DomainFileConfigDetail setAllowUploadFileCategoryList(java.util.List<String> allowUploadFileCategoryList) {
        this.allowUploadFileCategoryList = allowUploadFileCategoryList;
        return this;
    }
    public java.util.List<String> getAllowUploadFileCategoryList() {
        return this.allowUploadFileCategoryList;
    }

    public DomainFileConfigDetail setRecycleBinAutoDeleteEnabled(Boolean recycleBinAutoDeleteEnabled) {
        this.recycleBinAutoDeleteEnabled = recycleBinAutoDeleteEnabled;
        return this;
    }
    public Boolean getRecycleBinAutoDeleteEnabled() {
        return this.recycleBinAutoDeleteEnabled;
    }

    public DomainFileConfigDetail setRecycleBinAutoDeleteKeepSecond(Long recycleBinAutoDeleteKeepSecond) {
        this.recycleBinAutoDeleteKeepSecond = recycleBinAutoDeleteKeepSecond;
        return this;
    }
    public Long getRecycleBinAutoDeleteKeepSecond() {
        return this.recycleBinAutoDeleteKeepSecond;
    }

    public DomainFileConfigDetail setSameNameFileUploadMode(String sameNameFileUploadMode) {
        this.sameNameFileUploadMode = sameNameFileUploadMode;
        return this;
    }
    public String getSameNameFileUploadMode() {
        return this.sameNameFileUploadMode;
    }

    public DomainFileConfigDetail setSingleFileUploadSizeLimit(Long singleFileUploadSizeLimit) {
        this.singleFileUploadSizeLimit = singleFileUploadSizeLimit;
        return this;
    }
    public Long getSingleFileUploadSizeLimit() {
        return this.singleFileUploadSizeLimit;
    }

    public DomainFileConfigDetail setWebClientDownloadMode(String webClientDownloadMode) {
        this.webClientDownloadMode = webClientDownloadMode;
        return this;
    }
    public String getWebClientDownloadMode() {
        return this.webClientDownloadMode;
    }

}
