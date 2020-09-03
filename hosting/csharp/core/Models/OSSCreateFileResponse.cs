// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * Create file response
     */
    public class OSSCreateFileResponse : TeaModel {
        /// <summary>
        /// domain_id
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=false, MaxLength=50, Pattern="[a-z0-9]{1,50}")]
        public string DomainId { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// file_path
        /// </summary>
        [NameInMap("file_path")]
        [Validation(Required=false)]
        public string FilePath { get; set; }

        /// <summary>
        /// part_info_list
        /// </summary>
        [NameInMap("part_info_list")]
        [Validation(Required=false)]
        public List<UploadPartInfo> PartInfoList { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string ShareId { get; set; }

        /// <summary>
        /// type
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=false)]
        public string Type { get; set; }

        /// <summary>
        /// upload_id
        /// </summary>
        [NameInMap("upload_id")]
        [Validation(Required=false)]
        public string UploadId { get; set; }

    }

}
