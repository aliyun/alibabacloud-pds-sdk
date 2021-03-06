// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 文件移动请求
     */
    public class MoveFileRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// auto_rename
        /// </summary>
        [NameInMap("auto_rename")]
        [Validation(Required=false)]
        public bool? AutoRename { get; set; }

        [NameInMap("category_list")]
        [Validation(Required=false)]
        public List<string> CategoryList { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9.-_]{1,50}")]
        public string FileId { get; set; }

        [NameInMap("file_id_path")]
        [Validation(Required=false)]
        public string FileIdPath { get; set; }

        /// <summary>
        /// new_name
        /// </summary>
        [NameInMap("new_name")]
        [Validation(Required=false, MaxLength=1024)]
        public string NewName { get; set; }

        [NameInMap("share_id")]
        [Validation(Required=false)]
        public string ShareId { get; set; }

        /// <summary>
        /// to_drive_id
        /// </summary>
        [NameInMap("to_drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string ToDriveId { get; set; }

        /// <summary>
        /// to_parent_file_id
        /// </summary>
        [NameInMap("to_parent_file_id")]
        [Validation(Required=true, MaxLength=50)]
        public string ToParentFileId { get; set; }

        [NameInMap("to_share_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string ToShareId { get; set; }

    }

}
