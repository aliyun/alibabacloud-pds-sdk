<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class DefaultSetPasswordRequest extends Model
{
    public $headers;

    /**
     * @description App ID, 当前访问的App
     *
     * @example csaklidwasdhjwid
     *
     * @var string
     */
    public $appId;

    /**
     * @description AES-256对称加密密钥，通过App公钥加密后传输
     *
     * @example 123456,Abc
     *
     * @var string
     */
    public $encryptedKey;

    /**
     * @description 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
     *
     * @example 123456,Abc
     *
     * @var string
     */
    public $newPassword;

    /**
     * @description 修改密码的临时授权码
     *
     * @example abc
     *
     * @var string
     */
    public $state;
    protected $_name = [
        'appId'        => 'app_id',
        'encryptedKey' => 'encrypted_key',
        'newPassword'  => 'new_password',
        'state'        => 'state',
    ];

    public function validate()
    {
        Model::validateRequired('appId', $this->appId, true);
        Model::validateRequired('encryptedKey', $this->encryptedKey, true);
        Model::validateRequired('newPassword', $this->newPassword, true);
        Model::validateRequired('state', $this->state, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }
        if (null !== $this->encryptedKey) {
            $res['encrypted_key'] = $this->encryptedKey;
        }
        if (null !== $this->newPassword) {
            $res['new_password'] = $this->newPassword;
        }
        if (null !== $this->state) {
            $res['state'] = $this->state;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return DefaultSetPasswordRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['app_id'])) {
            $model->appId = $map['app_id'];
        }
        if (isset($map['encrypted_key'])) {
            $model->encryptedKey = $map['encrypted_key'];
        }
        if (isset($map['new_password'])) {
            $model->newPassword = $map['new_password'];
        }
        if (isset($map['state'])) {
            $model->state = $map['state'];
        }

        return $model;
    }
}
