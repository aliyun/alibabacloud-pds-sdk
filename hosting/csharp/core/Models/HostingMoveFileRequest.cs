// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 文件移动请求
     */
    public class HostingMoveFileRequest : TeaModel {
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
        /// new_name
        /// </summary>
        [NameInMap("new_name")]
        [Validation(Required=false)]
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
        /// file_path
        /// </summary>
        [NameInMap("to_parent_file_path")]
        [Validation(Required=false)]
        public string ToParentFilePath { get; set; }

    }

}
