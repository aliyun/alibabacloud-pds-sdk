// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * copy file request
     */
    public class OSSCopyFileRequest : TeaModel {
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
        [Validation(Required=true)]
        public string FilePath { get; set; }

        /// <summary>
        /// new_name
        /// </summary>
        [NameInMap("new_name")]
        [Validation(Required=false, Pattern="[a-zA-Z0-9.-]{1,1000}")]
        public string NewName { get; set; }

        /// <summary>
        /// overwrite
        /// type: boolean
        /// </summary>
        [NameInMap("overwrite")]
        [Validation(Required=false)]
        public bool? Overwrite { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false, Pattern="[0-9a-zA-Z-]+")]
        public string ShareId { get; set; }

        /// <summary>
        /// to_drive_id
        /// </summary>
        [NameInMap("to_drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string ToDriveId { get; set; }

        /// <summary>
        /// to_parent_file_path
        /// </summary>
        [NameInMap("to_parent_file_path")]
        [Validation(Required=true)]
        public string ToParentFilePath { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("to_share_id")]
        [Validation(Required=false)]
        public string ToShareId { get; set; }

    }

}
