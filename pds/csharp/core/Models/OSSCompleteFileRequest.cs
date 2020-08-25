// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * complete file request
     */
    public class OSSCompleteFileRequest : TeaModel {
        /// <summary>
        /// addition_data
        /// </summary>
        [NameInMap("addition_data")]
        [Validation(Required=false)]
        public Dictionary<string, object> AdditionData { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        [NameInMap("file_path")]
        [Validation(Required=false)]
        public string FilePath { get; set; }

        /// <summary>
        /// forbid_overwrite
        /// type: boolean
        /// </summary>
        [NameInMap("forbid_overwrite")]
        [Validation(Required=false)]
        public bool? ForbidOverwrite { get; set; }

        /// <summary>
        /// part_info_list
        /// </summary>
        [NameInMap("part_info_list")]
        [Validation(Required=false)]
        public List<UploadPartInfo> PartInfoList { get; set; }

        [NameInMap("share_id")]
        [Validation(Required=false)]
        public string ShareId { get; set; }

        /// <summary>
        /// upload_id
        /// </summary>
        [NameInMap("upload_id")]
        [Validation(Required=false)]
        public string UploadId { get; set; }

    }

}
